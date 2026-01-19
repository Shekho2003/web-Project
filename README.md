<div align="center">

# 🎬 **Sinema ve İzleyici Segmentasyonu (V2.0)**  
## 🔍 **Araştırma Soruları**

> 🎯 Bu proje, izleyici davranışlarını anlamak ve film pazarlama stratejilerini veriyle güçlendirmek amacıyla üç temel soruya odaklanır:

1. **Filmimizi kimler izliyor ve yorum yapıyor?**  
   (Sinefiller mi, fan kitlesi mi, yoksa genel izleyiciler mi?)  
2. **Kampanyalarda hangi öge öne çıkarılmalı?**  
   (Senaryo derinliği mi, yoksa görsel efektler mi?)  
3. **Sadık kitlemizin ortak özellikleri nelerdir?**

---

## 🧠 **Proje Özeti**

🎥 Bu çalışma, **YouTube** üzerindeki film yorumlarını analiz ederek, izleyici gruplarının **duygusal eğilimlerini** ve **segment profillerini** ortaya çıkarmaktadır.  
Amaç, bir filmin kimler tarafından, hangi gerekçelerle beğenildiğini veya eleştirildiğini anlamaktır.  

💡 Yapay zekâ destekli analiz sonucunda izleyiciler dört ana kategoriye ayrılmıştır:
- 🎬 **Sinefil / Hikaye Odaklı**  
- ⚡ **Görsel / Aksiyon Sever**  
- 🌟 **Fan Kitlesi / Oyuncu Odaklı**  
- 👥 **Genel İzleyici (Hype/Tepki)**  

---

## 📊 **1. Yöntem ve Veri Süreci**

| Aşama | Açıklama |
|:--|:--|
| 🧩 **Veri Toplama** | YouTube API ile **40.000** film yorumu toplanmıştır. |
| 🧮 **Duygu Analizi** | TextBlob ve kelime tabanlı sınıflandırmayla pozitif, negatif, nötr olarak etiketlenmiştir. |
| 🎭 **Segmentasyon** | Yorum kelimelerine göre 4 ana izleyici grubu belirlenmiştir. |
| 📈 **Raporlama** | Pandas & Matplotlib ile sonuçlar tablo ve grafik olarak sunulmuştur. |

---

## 💬 **2. Bulgular ve Görseller**

### 🎞️ **Genel Duygu Dağılımı**
Toplam **40.000 YouTube yorumu** analiz edilmiştir.

| Duygu | Yorum Sayısı | Oran |
|:--|:--|:--|
| 🍿 Olumlu (Beğeni) | 16.425 | %41.1 |
| 🍅 Olumsuz (Eleştiri) | 4.656 | %11.6 |
| 😐 Nötr / Kararsız | 18.919 | %47.3 |



> **Yorumların %41’i olumlu, %11’i olumsuzdur.**  
> İzleyicilerin çoğu filmi analitik ve temkinli bir biçimde değerlendirmiştir.

---

### 🧭 **İzleyici Segmentlerinin Davranış Profili**

| Segment | Pozitif | Negatif | Özellik |
|:--|:--:|:--:|:--|
| 👥 Genel İzleyici | 6.474 | 1.602 | Beklenti, tepki, genel görüş |
| ⚡ Görsel/Aksiyon Sever | 2.389 | 501 | Efekt, sahne, aksiyon odaklı |
| 🎬 Sinefil | 1.638 | 418 | Senaryo, karakter derinliği |
| 🌟 Fan Kitlesi | — | — | Oyuncu ve karakter sadakati |

![Genel Duygu Dağılımı](./Ekran%20Görüntüsü%20(47).png)

> **Fan Kitlesi** duygusal yoğunluğu en yüksek gruptur.  
> **Sinefiller** ise analitik-eleştirel yaklaşımıyla film derinliğine odaklanır.

---

## 💡 **3. Stratejik Çıkarımlar**

✅ **İzleyici kitlesi tek tip değildir.**  
Her segment farklı duygusal ve tematik önceliklere sahiptir.

🎯 **Kampanya önerileri:**
- Aksiyon Sever → Görsel kalite ve tempo vurgusu  
- Sinefil → Hikaye anlatımı ve derinlik  
- Fan Kitlesi → Oyuncu, karakter ve duygusal bağlılık  

📊 **Veri temelli kişiselleştirme**, film pazarlamasında başarı oranını artırır.

---

## 🔭 **4. Gelecek Çalışmalar İçin Öneriler**

| Alan | Açıklama |
|:--|:--|
| ⏳ **Zaman Serisi Analizi** | Film vizyon öncesi ve sonrası duygu değişimleri incelenebilir. |
| 🎞️ **Tür Bazlı Segmentasyon** | Türlere göre izleyici farkları araştırılabilir. |
| 🌐 **Platform Genişletme** | Gelecekte TikTok, X (Twitter) veya IMDb verileri eklenebilir. |
| 🧠 **Derin Öğrenme Analizi** | İroni, nostalji, hayal kırıklığı gibi duygular tespit edilebilir. |

---

## ⚙️ **Kullanılan Teknolojiler**

<p align="center">
<img src="https://img.shields.io/badge/Python-blue?logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/YouTube%20Data%20API-red?logo=youtube"/>
<img src="https://img.shields.io/badge/Pandas%20%26%20Matplotlib-green"/>
<img src="https://img.shields.io/badge/TQDM-gray"/>
</p>

---

## 📁 **Proje Dosyaları**

