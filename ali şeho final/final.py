import time, re, os
from collections import Counter
from urllib.parse import urlparse, parse_qs
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
from tqdm import tqdm
from textblob import TextBlob
from langdetect import detect

# =============================================================================
## 1. AYARLAR VE KELİME SÖZLÜKLERİ (Sinema ve İzleyici Segmentasyonu İÇİN)
# =============================================================================

AUDIENCE_SEGMENTS = {
    "Sinefil / Hikaye Odaklı": [
        "senaryo", "hikaye", "kurgu", "plot", "story", "script", "writing", "karakter", 
        "derinlik", "felsefe", "mesaj", "anlatım", "dialogue", "diyalog", "twist", "sonu", 
        "final", "mantık", "boşluk", "cliche", "klişe"
    ],
    "Görsel / Aksiyon Sever": [
        "efekt", "cgi", "vfx", "görsel", "visual", "aksiyon", "action", "sahne", "kavga", 
        "patlama", "fight", "renk", "sinematografi", "çekim", "kamera", "atmosfer", "3d", "imax", 
        "ses", "soundtrack", "müzik"
    ],
    "Oyuncu / Fan Kitlesi": [
        "oyuncu", "aktör", "aktris", "cast", "acting", "oyunculuk", "performans", "yakışıklı", 
        "güzel", "kral", "queen", "fan", "hayran", "abi", "abla", "role", "rol", "karizma"
    ],
    "Genel İzleyici (Hype/Tepki)": [
        "hype", "bekliyorum", "heyecan", "sıkıcı", "boring", "zaman", "vakit", "bilet", 
        "sinema", "film", "movie", "izledim", "izlenir", "tavsiye", "fragman", "trailer", "çöp", "efsane"
    ]
}

SENTIMENT_OVERRIDE = {
    "POSITIVE": ["masterpiece", "başyapıt", "efsane", "mükemmel", "harika", "best", "oscar", "büyüleyici", "soluksuz", "bayıldım", "şahane", "10/10", "hype", "bekliyorum"],
    "NEGATIVE": ["berbat", "çöp", "trash", "worst", "hayal kırıklığı", "disappoint", "sıkıcı", "boşa", "uyumuşum", "felaket", "rezalet", "cringe", "zaman kaybı"]
}

# Analiz dışı bırakılacak kelimeler (Stopwords)
STOPWORDS = set(['bir', 've', 'bu', 'da', 'de', 'çok', 'ama', 'için', 'ben', 'sen', 'o', 'the', 'and', 'is', 'to', 'in', 'of', 'it', 'film', 'movie'])

# =============================================================================
# 2. YARDIMCI FONKSİYONLAR
# =============================================================================

def get_video_id(url):
    if not url: return None
    m = re.search(r'(?:youtu\.be/|v=|/v/|embed/)([A-Za-z0-9_-]{11})', url)
    return m.group(1) if m else parse_qs(urlparse(url).query).get('v', [None])[0]

def preprocess_text(text):
    """Metni temizler."""
    if not isinstance(text, str): return ""
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+', '', text)
    text = text.replace('\n', ' ').replace('\r', ' ')
    # Sadece harf ve sayıları bırak (Daha temiz kelime analizi için)
    # text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze_cinema_row(text):
    clean_text = preprocess_text(text)
    
    # Boş veri kontrolü
    if not clean_text or len(clean_text) < 2:
        return clean_text, "Bilinmiyor", "Neutral", 0.0, "Belirsiz"

    # --- 1. Dil Tespiti ---
    lang = "Bilinmiyor"
    try: 
        if len(clean_text) > 3: lang = detect(clean_text).upper()
    except: pass
    
    # --- 2. Duygu Analizi ---
    blob = TextBlob(clean_text)
    score = blob.sentiment.polarity
    text_lower = clean_text.lower()
    
    s_class = "Neutral"
    # Override Kuralları
    if any(w in text_lower for w in SENTIMENT_OVERRIDE["POSITIVE"]):
        s_class = "Positive"; score = 0.9
    elif any(w in text_lower for w in SENTIMENT_OVERRIDE["NEGATIVE"]):
        s_class = "Negative"; score = -0.9
    else:
        if score > 0.05: s_class = "Positive"
        elif score < -0.05: s_class = "Negative"

    # --- 3. İzleyici Segmentasyonu ---
    detected_segments = []
    for segment, keywords in AUDIENCE_SEGMENTS.items():
        if any(k in text_lower for k in keywords):
            detected_segments.append(segment)
    
    segment_str = ", ".join(detected_segments) if detected_segments else "Belirsiz / Sessiz İzleyici"
    
    return clean_text, lang, s_class, score, segment_str

# =============================================================================
# 3. VERİ ÇEKME MOTORU
# =============================================================================

def add_comment_to_list(comments_list, seen_set, cid, snippet, parent_id=None):
    if cid in seen_set: return False
    raw_text = snippet.get('textDisplay', "")
    if not raw_text: return False

    clean, lang, s_class, s_score, segment = analyze_cinema_row(raw_text)

    # Çok kısa veya boş yorumları listeye ekleme (Veri Ön İşleme)
    if not clean: return False

    row = {
        'ID': cid,
        'Tip': "Yanıt" if parent_id else "Ana Yorum",
        'Yazar': snippet.get('authorDisplayName'),
        'Orjinal_Yorum': raw_text,
        'Temizlenmis_Yorum': clean,
        'Begeni': int(snippet.get('likeCount', 0)),
        'Tarih': snippet.get('publishedAt'),
        'Dil': lang,
        'Duygu_Sinifi': s_class,
        'Duygu_Skoru': round(s_score, 2),
        'Izleyici_Segmenti': segment
    }
    comments_list.append(row)
    seen_set.add(cid)
    return True

def fetch_replies_deep(yt, parent_id, seen_set, comments_list, max_limit):
    token = None
    while len(comments_list) < max_limit:
        try:
            req = yt.comments().list(
                part="snippet", parentId=parent_id, maxResults=100, pageToken=token, textFormat="plainText"
            )
            res = req.execute()
            if not res.get('items'): break
            for item in res['items']:
                if len(comments_list) >= max_limit: return
                add_comment_to_list(comments_list, seen_set, item['id'], item['snippet'], parent_id)
            token = res.get('nextPageToken')
            if not token: break
            time.sleep(0.05)
        except: break

def master_fetch(api_key, video_id, target_count):
    try:
        yt = build('youtube', 'v3', developerKey=api_key)
    except Exception as e:
        print(f"\n❌ API Bağlantı Hatası: {e}"); return []

    all_comments = []
    seen_ids = set()
    print(f"\n🚀 SİNEMA VERİSİ ÇEKİLİYOR... Hedef: {target_count}")
    
    for order in ['relevance', 'time']:
        if len(all_comments) >= target_count: break
        token = None
        pbar = tqdm(total=target_count, unit=" yorum", initial=len(all_comments), desc=f"Mod: {order.upper()}")
        while len(all_comments) < target_count:
            try:
                req = yt.commentThreads().list(
                    part="snippet,replies", videoId=video_id, maxResults=100, 
                    pageToken=token, textFormat="plainText", order=order
                )
                res = req.execute()
                if not res.get('items'): break
                for item in res['items']:
                    if len(all_comments) >= target_count: break
                    top_snip = item['snippet']['topLevelComment']['snippet']
                    top_id = item['id']
                    if add_comment_to_list(all_comments, seen_ids, top_id, top_snip):
                        pbar.update(1)
                    reply_count = item['snippet']['totalReplyCount']
                    if reply_count > 0 and 'replies' in item:
                        for rep in item['replies']['comments']:
                            if len(all_comments) >= target_count: break
                            add_comment_to_list(all_comments, seen_ids, rep['id'], rep['snippet'], top_id)
                            pbar.update(1)
                        if reply_count > len(item.get('replies', {}).get('comments', [])):
                            fetch_replies_deep(yt, top_id, seen_ids, all_comments, target_count)
                            pbar.n = len(all_comments); pbar.refresh()
                token = res.get('nextPageToken')
                if not token: break
            except HttpError as e:
                if "quotaExceeded" in str(e): print("\n⚠️ API KOTASI DOLDU!"); return all_comments
                if e.resp.status == 403: return all_comments
                time.sleep(1)
            except Exception as e:
                print(f"Hata: {e}"); time.sleep(1)
        pbar.close()
    return all_comments

# =============================================================================
# 4. DETAYLI İÇERİK ANALİZİ FONKSİYONLARI
# =============================================================================

def analyze_content_details(df_subset, label):
    """
    Belirli bir veri kümesi (Örn: Sadece Olumlular) için detaylı analiz yapar.
    """
    if df_subset.empty:
        print(f"   ⚠️ {label} için yeterli veri yok.")
        return

    # 1. En Çok Konuşulan Konular (Segmentler üzerinden)
    segments = df_subset['Izleyici_Segmenti'].str.split(', ').explode()
    # "Belirsiz" olanları çıkar, çünkü konuyu anlamaya çalışıyoruz
    segments = segments[segments != "Belirsiz / Sessiz İzleyici"]
    
    print(f"\n   📌 {label} NE HAKKINDA KONUŞUYOR? (Top 3 Konu)")
    if not segments.empty:
        for seg, count in segments.value_counts().head(3).items():
            print(f"      🔹 {seg}: {count} kez")
    else:
        print("      (Konu tespiti yapılamadı)")

    # 2. En Sık Kullanılan Kelimeler (Word Frequency)
    text_blob = " ".join(df_subset['Temizlenmis_Yorum'].astype(str)).lower()
    # Noktalama işaretlerini kaldır
    text_blob = re.sub(r'[^\w\s]', '', text_blob)
    words = text_blob.split()
    # Stopwords temizliği
    clean_words = [w for w in words if w not in STOPWORDS and len(w) > 2]
    
    most_common = Counter(clean_words).most_common(5)
    
    print(f"\n   💬 {label} EN ÇOK HANGİ KELİMELERİ KULLANIYOR?")
    if most_common:
        print(f"      👉 {', '.join([f'{w[0]} ({w[1]})' for w in most_common])}")
    else:
        print("      (Yeterli kelime verisi yok)")

# =============================================================================
# 5. RAPORLAMA
# =============================================================================

def generate_cinema_report(df):
    print("\n" + "="*60)
    print("🎬 SİNEMA & İZLEYİCİ SEGMENTASYON RAPORU (V2.0)")
    print("="*60)
    
    total = len(df)
    if total == 0: print("Veri yok."); return

    print(f"\n👥 Toplam İşlenen Yorum: {total}")

    # --- DUYGU ORANLARI ---
    pos_df = df[df['Duygu_Sinifi'] == 'Positive']
    neg_df = df[df['Duygu_Sinifi'] == 'Negative']
    
    print("\n📊 GENEL DUYGU DURUMU:")
    print(f"   🍿 Olumlu (Beğeni): {len(pos_df)} (%{len(pos_df)/total*100:.1f})")
    print(f"   🍅 Olumsuz (Eleştiri): {len(neg_df)} (%{len(neg_df)/total*100:.1f})")

    # --- DETAYLI POZİTİF ANALİZ ---
    print("\n" + "-"*40)
    print("🟢 POZİTİF YORUMLARIN İÇERİK ANALİZİ")
    print("-" * 40)
    analyze_content_details(pos_df, "BEĞENENLER")

    # --- DETAYLI NEGATİF ANALİZ ---
    print("\n" + "-"*40)
    print("🔴 NEGATİF YORUMLARIN İÇERİK ANALİZİ")
    print("-" * 40)
    analyze_content_details(neg_df, "ELEŞTİRENLER")

    print("\n" + "="*60)

# =============================================================================
# 6. MAIN
# =============================================================================

def main():
    print("🎥 SİNEMA ANALİZ ARACI (V2.0) BAŞLATILIYOR...")
    api_key = input("🔑 API KEY: ").strip()
    url = input("🔗 Video URL: ").strip()
    try: target = int(input("🔢 Hedef (Enter=2000): ") or 2000)
    except: target = 2000
    
    vid = get_video_id(url)
    if not vid: print("❌ Hatalı Link"); return

    data = master_fetch(api_key, vid, target)
    
    if data:
        df = pd.DataFrame(data)
        fname = f"Sinema_Analiz_{int(time.time())}.xlsx"
        df.to_excel(fname, index=False)
        print(f"\n✅ Veriler kaydedildi: {fname}")
        generate_cinema_report(df)
    else:
        print("\n❌ Veri çekilemedi.")

if __name__ == "__main__":
    main()