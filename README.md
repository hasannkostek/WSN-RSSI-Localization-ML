WSN-RSSI-Localization-ML 📡🤖
Kablosuz Sensör Ağlarında RSSI ve Makine Öğrenmesi (KNN) ile Konum Belirleme Simülasyonu

Bu proje, GPS sinyalinin ulaşamadığı veya maliyetli olduğu senaryolarda (madenler, depolar, akıllı tarım alanları), düğümlerden gelen sinyal gücü (RSSI) verilerini kullanarak sensör konumlarını yüksek doğrulukla tahmin eden Python tabanlı bir simülatördür. 

🚀 Projenin Öne Çıkan Özellikleri

Log-Distance Path Loss Modeli: Radyo sinyallerinin mesafeye bağlı sönümlenmesi ve çevresel gürültü (Gaussian Noise) matematiksel olarak modellenmiştir. 
Makine Öğrenmesi Entegrasyonu: Trilaterasyon gibi klasik yöntemlerin aksine, gürültülü veriyi sönümleyebilen K-Nearest Neighbors (KNN) Regressor kullanılmıştır. 
Kapsamlı Hata Analizi: Tahmin edilen koordinatlar ile gerçek koordinatlar arasındaki fark (Euclidean Distance) üzerinden sistem başarımı test edilmiştir. 
Görselleştirme: Dinamik harita çıktıları ve hata dağılım grafikleri ile sonuçlar raporlanmıştır. 


🛠️ Kullanılan Teknolojiler ve Kütüphaneler

Python: Temel programlama dili. 
NumPy: Matris işlemleri ve veri manipülasyonu. 
Scikit-learn: KNN algoritması ve model eğitimi. 
Matplotlib: Sonuçların 2D harita ve grafiklerle görselleştirilmesi. 
Math: Logaritmik sinyal kaybı formülasyonu.

📊 Örnek Sonuçlar
Simülasyon 100x100 metrelik bir alanda 500 eğitim verisi ile gerçekleştirilmiştir. Yapılan 20 bağımsız test sonucunda:
Ortalama Hata Payı: ~2.5 - 3.5 Metre (Gürültü oranına bağlı olarak).
Zaman Karmaşıklığı: O(n) (Hızlı tahmin süresi).

<img width="586" height="592" alt="image" src="https://github.com/user-attachments/assets/2aedac62-c548-4cba-8c15-4c1a4ee92221" />
<img width="850" height="698" alt="Ekran görüntüsü 2026-02-27 142353" src="https://github.com/user-attachments/assets/528e8145-b6b4-470b-a48c-8b323e529200" />
<img width="842" height="470" alt="Ekran görüntüsü 2026-02-27 142406" src="https://github.com/user-attachments/assets/53595ba6-7533-47d0-89ab-cc1459982b4c" />




👨‍💻 Yazar
Hasan Köstek
