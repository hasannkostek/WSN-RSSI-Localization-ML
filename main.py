#1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

#2
3
# Referans düğümlerin koordinatları (Köşeler)
# [x, y] formatında
anchors = np.array([[0, 0], [100, 0], [0, 100], [100, 100]])

# Haritayı çizdirelim
plt.figure(figsize=(6,6))
plt.scatter(anchors[:, 0], anchors[:, 1], c='red', marker='^', s=100, label='Referans Düğümler')
plt.xlim(-10, 110)
plt.ylim(-10, 110)
plt.legend()
plt.title("WSN Simülasyon Alanı")
plt.show()


#3
import math

def rssi_hesapla(mesafe):
    A = -40  # 1 metredeki sinyal gücü (sabit)
    n = 2    # Ortam katsayısı (boş alan için 2)
    
    if mesafe == 0: return A # Mesafe 0 ise hata almamak için
    
    # Formülümüz: RSSI = -(10 * n * log10(d) - A) 
    # Not: A zaten negatif olduğu için matematiksel olarak toplama/çıkarma yönüne dikkat edilir.
    rssi = A - (10 * n * math.log10(mesafe))
    
    # Gerçekçilik için üzerine biraz rastgele "Gürültü" (Noise) ekleyelim
    gurultu = np.random.normal(0, 2) # 2 birimlik standart sapma ile rastgele hata
    return rssi + gurultu




#4
X_train = [] # Sinyal güçleri (Girdiler)
y_train = [] # Gerçek koordinatlar (Çıktılar/Etiketler)

for _ in range(500): # 500 tane örnek üret
    # 100x100 alanda rastgele bir X ve Y koordinatı seç
    rastgele_x = np.random.uniform(0, 100)
    rastgele_y = np.random.uniform(0, 100)
    nokta = np.array([rastgele_x, rastgele_y])
    
    # Bu noktanın 4 referans düğümüne (anchors) olan uzaklıklarına göre RSSI değerlerini bul
    sinyal_gucleri = []
    for anchor in anchors:
        mesafe = np.linalg.norm(nokta - anchor) # İki nokta arası Öklid mesafesi
        sinyal_gucleri.append(rssi_hesapla(mesafe))
    
    X_train.append(sinyal_gucleri)
    y_train.append([rastgele_x, rastgele_y])

X_train = np.array(X_train)
y_train = np.array(y_train)

print("Eğitim verileri hazır! 500 örnek oluşturuldu.")



#5
# KNN Regressor modelini oluşturuyoruz
# n_neighbors=5: En yakın 5 benzer örneğe bakarak konum tahmini yap demek
model = KNeighborsRegressor(n_neighbors=5)

# Modeli elimizdeki verilerle eğitiyoruz
model.fit(X_train, y_train)

print("Yapay zeka başarıyla eğitildi! Artık konum tahmin edebilir.")




#6
# 1. Test için rastgele bir gerçek nokta belirleyelim
gercek_konum = np.array([[30.0, 70.0]]) # Örn: X=30, Y=70

# 2. Bu noktanın referanslara olan sinyal gücünü ölçelim
test_sinyalleri = []
for anchor in anchors:
    d = np.linalg.norm(gercek_konum - anchor)
    test_sinyalleri.append(rssi_hesapla(d))

# 3. Yapay zekaya tahmin ettirelim
tahmin_edilen = model.predict([test_sinyalleri])

print(f"Gerçek Konum: {gercek_konum[0]}")
print(f"Tahmin Edilen Konum: {tahmin_edilen[0]}")

# Hata miktarını (metre cinsinden mesafe farkı) hesaplayalım
hata = np.linalg.norm(gercek_konum - tahmin_edilen)
print(f"Hata Payı: {hata:.2f} metre")






#7
plt.figure(figsize=(10, 8))

# 1. Referans Düğümleri çizelim (Kırmızı Üçgenler)
plt.scatter(anchors[:, 0], anchors[:, 1], c='red', marker='^', s=150, label='Referans Düğümler (Anchors)')

# 2. Gerçek Konumu çizelim (Mavi Yıldız)
plt.scatter(gercek_konum[0][0], gercek_konum[0][1], c='blue', marker='*', s=200, label='Gerçek Konum')

# 3. Yapay Zekanın Tahminini çizelim (Yeşil Nokta)
plt.scatter(tahmin_edilen[0][0], tahmin_edilen[0][1], c='green', marker='o', s=100, label='AI Tahmini')

# 4. Hata Çizgisi (Gerçek ve Tahmin arasına siyah kesikli çizgi)
plt.plot([gercek_konum[0][0], tahmin_edilen[0][0]], 
         [gercek_konum[0][1], tahmin_edilen[0][1]], 
         'k--', alpha=0.6, label=f'Hata Mesafesi: {hata:.2f}m')

# Estetik Ayarlar
plt.title("WSN Konumlandırma: Gerçek vs Tahmin", fontsize=14)
plt.xlabel("X Koordinatı (Metre)")
plt.ylabel("Y Koordinatı (Metre)")
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper right')
plt.xlim(-5, 105)
plt.ylim(-5, 105)

plt.show()



#8
test_nokta_sayisi = 20
toplam_hata = 0
hata_listesi = []

print(f"{'No':<5} | {'Gerçek (X,Y)':<20} | {'Tahmin (X,Y)':<20} | {'Hata (m)':<10}")
print("-" * 65)

for i in range(test_nokta_sayisi):
    # Rastgele gerçek konumlar üret
    gx, gy = np.random.uniform(0, 100), np.random.uniform(0, 100)
    gercek = np.array([gx, gy])
    
    # Sinyal güçlerini ölç
    test_rssi = [rssi_hesapla(np.linalg.norm(gercek - a)) for a in anchors]
    
    # AI Tahmini
    tahmin = model.predict([test_rssi])[0]
    
    # Hata hesapla
    mesafe_hatasi = np.linalg.norm(gercek - tahmin)
    hata_listesi.append(mesafe_hatasi)
    toplam_hata += mesafe_hatasi
    
    print(f"{i+1:<5} | {str(np.round(gercek,1)):<20} | {str(np.round(tahmin,1)):<20} | {mesafe_hatasi:.2f}")

ortalama_hata = toplam_hata / test_nokta_sayisi
print("-" * 65)
print(f"SİSTEM GENEL PERFORMANSI (Ortalama Hata): {ortalama_hata:.2f} Metre")







#9
plt.figure(figsize=(10, 5))
plt.bar(range(1, test_nokta_sayisi + 1), hata_listesi, color='skyblue')
plt.axhline(y=ortalama_hata, color='red', linestyle='--', label=f'Ortalama Hata: {ortalama_hata:.2f}m')
plt.xlabel("Test Edilen Nokta No")
plt.ylabel("Hata Mesafesi (Metre)")
plt.title("Sistemin Konumlandırma Hassasiyeti")
plt.legend()
plt.show()

# HASAN KÖSTEK