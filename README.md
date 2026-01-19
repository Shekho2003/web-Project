🎬 Sinema ve İzleyici Segmentasyonu (V2.0 – YouTube Yorum Analizi)
🔍 Araştırma Soruları

Bu proje aşağıdaki üç temel soruya yanıt aramaktadır:

Filmimizi kimler izliyor ve yorum yapıyor?
(Sinefiller mi, fan kitlesi mi, yoksa sadece genel izleyiciler mi?)

Pazarlama kampanyasında hangi unsuru öne çıkarmalıyız?
(Senaryo derinliği mi, yoksa görsel efektlerin kalitesi mi?)

Sadık izleyici gruplarının ortak özellikleri nelerdir?

📌 Proje Özeti

Bu proje, YouTube üzerindeki film yorumlarını analiz ederek sinema izleyicilerini duygusal eğilim ve segment profiline göre sınıflandırmaktadır.
Amaç, izleyicilerin filmi hangi yönleriyle değerlendirdiğini ve pazarlama stratejilerinin buna nasıl uyarlanabileceğini ortaya koymaktır.

Veriler, YouTube API aracılığıyla toplanmış ve Python dili kullanılarak işlenmiştir.
Yapay zekâ destekli metin analizi ile yorumlar dört temel kategoriye ayrılmıştır:

Sinefil / Hikaye Odaklı

Görsel / Aksiyon Sever

Fan Kitlesi / Oyuncu Odaklı

Genel İzleyici (Hype/Tepki)

🧩 1. Yöntem ve Veri Süreci
Aşama	Açıklama
Aşama 1: Veri Toplama	YouTube API ile 40.000 film yorumu toplanmıştır. Her yorum için tarih, beğeni sayısı, dil ve yazar bilgisi kaydedilmiştir.
Aşama 2: Duygu Analizi	TextBlob ve kelime tabanlı sınıflandırma yöntemiyle yorumlar pozitif, negatif ve nötr olarak etiketlenmiştir.
Aşama 3: İzleyici Segmentasyonu	Yorum metinlerinde geçen kelimelere göre izleyiciler dört segmente ayrılmıştır.
Aşama 4: Raporlama ve Görselleştirme	Pandas ve Matplotlib ile sonuçlar tablo ve grafik formatında raporlanmıştır.
📊 2. Bulgular ve Görseller
🎞️ Genel Duygu Dağılımı

Toplam 40.000 YouTube yorumu analiz edilmiştir.

Duygu	Yorum Sayısı	Oran
🍿 Olumlu (Beğeni)	16.425	%41.1
🍅 Olumsuz (Eleştiri)	4.656	%11.6
😐 Nötr / Kararsız	18.919	%47.3

📈 Grafik 1: Genel Duygu Dağılımı


Yorumların %41,1’i olumlu, %11,6’sı olumsuz, %47,3’ü nötr tondadır.
Bu durum, izleyicilerin büyük kısmının filmi analitik biçimde değerlendirdiğini göstermektedir.

🧠 İzleyici Segmentlerinin Davranış Profili

📈 Grafik 2: İzleyici Segmentlerinin Davranış Profili (Radar Analizi)


Segment	Pozitif Yorum Sayısı	Negatif Yorum Sayısı	Belirgin Özellik
Genel İzleyici (Hype/Tepki)	6.474	1.602	Beklenti, tepki, genel görüş
Görsel / Aksiyon Sever	2.389	501	Efekt, sahne, aksiyon odaklı
Sinefil / Hikaye Odaklı	1.638	418	Senaryo ve karakter derinliği
Fan Kitlesi / Oyuncu Odaklı	—	—	Oyuncular, karakter sadakati

Genel izleyici ve aksiyon sever grupları en yüksek pozitif oranlara sahiptir.
Sinefiller ise eleştirel eğilimleriyle denge unsuru oluşturur.

💡 3. Stratejik Yorumlar ve Öneriler

İzleyici kitlesi tek tip değildir; her segment farklı duygusal ve tematik beklentilere sahiptir.

Fan kitlesi, en yüksek sadakat ve duygusal bağlılığı gösteren segmenttir.

Sinefiller senaryo derinliğine, Aksiyon Severler ise görselliğe önem vermektedir.

Veri temelli pazarlama, her izleyici segmenti için özelleştirilmiş iletişim dili gerektirir.

Film kampanyalarında:

Aksiyon severler için görsel kalite ve tempo,

Sinefiller için hikaye anlatımı,

Fan kitlesi için karakter ve oyuncu vurgusu ön plana çıkarılmalıdır.

🔭 4. Gelecek Çalışmalar İçin Öneriler

Zaman Serisi Analizi:
Film vizyon öncesi ve sonrası duygu değişimleri incelenebilir.

Tür Bazlı Segmentasyon:
Aksiyon, dram ve bilim kurgu türlerinde izleyici farkları araştırılabilir.

Platform Genişletme:
Bu proje yalnızca YouTube verisine dayanmaktadır.
Gelecekte TikTok, X (Twitter) ve IMDb verileriyle genişletilebilir.

Derin Öğrenme Duygu Analizi:
İroni, nostalji, hayal kırıklığı gibi karmaşık duygular derin modellerle tespit edilebilir.

🛠️ 5. Kullanılan Teknolojiler

Python

Google YouTube Data API

Pandas

Matplotlib

TQDM

👨‍💻 6. Proje Dosyaları
📂 SinemaSegmentAnalizi_V2/
 ├── cinema_analysis_v2.py         # Güncellenmiş analiz scripti
 ├── grafik1_v2.png                # Genel Duygu Dağılımı
 ├── grafik2_radar_v2.png          # Davranış Profili (Radar)
 ├── Sinema_Analiz_1768835096.xlsx # Çıktı verisi
 ├── README.md                     # Bu dosya

🏁 7. Genel Sonuç

Bu proje, YouTube’daki 40.000 film yorumunun analiz edilmesiyle,
izleyici gruplarının duygusal eğilimlerini ve davranışsal profillerini ortaya koymuştur.

Genel izleyici ve aksiyon severler pozitif eğilimli kitleyi oluştururken,
sinefiller analitik-eleştirel dengeyi,
fan kitlesi ise en yüksek sadakati temsil etmektedir.

Sonuç olarak, sinema sektöründe veri destekli segment bazlı kampanyalar,
izleyici memnuniyetini ve etkileşimi artırmak için güçlü bir araçtır.

📎 Görselleri GitHub’a yüklerken:

grafik1_v2.png → Grafik 1 (Genel Duygu Dağılımı)

grafik2_radar_v2.png → Grafik 2 (Radar Analizi)

README’nin ilgili kısımlarına şu şekilde ekleyebilirsin:

![Grafik 1](grafik1_v2.png)
![Grafik 2](grafik2_radar_v2.png)

✅ Minimum Başarı Kriteri Karşılaştırması
Kriter	Hedef	Durum
Veri kaynağı	En az 1 sosyal medya platformu	✅ YouTube
Duygu analizi	Pozitif/Negatif/Nötr sınıflandırma	✅ Var
Segmentasyon	Kullanıcı gruplarının belirlenmesi	✅ 4 segment
Görsel içerik	En az 1 grafik	✅ 2 profesyonel grafik
Raporlama	Açıklayıcı metin + sonuç + öneri	✅ Eksiksiz
Gelecek çalışmalar	Araştırma vizyonu	✅ Yazılmış
