# odev_matris.py
# Veri Yapıları ve Algoritmalar - Matris İşlemleri Ödevi

def main():
    # ==========================================
    # BÖLÜM 1: Matris Oluşturma
    # ==========================================
    n = int(input("Matris boyutu (n): "))
    matris = []
    
    print(f"\nLütfen {n}x{n} elemanları girin (Her satırı aralarında boşluk bırakarak yazıp Enter'a basın):")
    for i in range(n):
        # Kullanıcıdan string olarak alınan satırı boşluklardan ayırıp tam sayıya (int) çeviriyoruz
        satir = list(map(int, input().split()))
        matris.append(satir)

    # ==========================================
    # BÖLÜM 2: Matrisi Yazdırma
    # ==========================================
    print("\nMatris:\n")
    # Matrisin satırlarında (i) ve sütunlarında (j) gezinmek için iç içe döngü
    for i in range(n):
        for j in range(n):
            print(matris[i][j], end=" ")
        print() # Her satır bittiğinde alt satıra geçmek için

    # ==========================================
    # BÖLÜM 3: Matris Toplamı
    # ==========================================
    genel_toplam = 0
    for i in range(n):
        for j in range(n):
            genel_toplam += matris[i][j]
    print(f"\nMatris toplamı: {genel_toplam}")

    # ==========================================
    # BÖLÜM 4: Köşegen Elemanları
    # ==========================================
    print("\nAna köşegen:\n")
    # Ana köşegende satır ve sütun indeksleri birbirine eşittir (0,0 - 1,1 - 2,2 vb.)
    for i in range(n):
        print(matris[i][i])

    # ==========================================
    # BÖLÜM 5: En Büyük Eleman
    # ==========================================
    # İlk elemanı en büyük kabul edip diğerleriyle kıyaslıyoruz
    en_buyuk = matris[0][0]
    for i in range(n):
        for j in range(n):
            if matris[i][j] > en_buyuk:
                en_buyuk = matris[i][j]
    print(f"\nMatrisin en büyük sayısı: {en_buyuk}")

    # ==========================================
    # BÖLÜM 6: Satır Toplamları
    # ==========================================
    for i in range(n):
        satir_toplami = 0
        for j in range(n):
            satir_toplami += matris[i][j]
        print(f"{i + 1}. satır toplamı: {satir_toplami}")

    # ==========================================
    # BONUS BÖLÜM (İsteğe Bağlı Özellikler)
    # ==========================================
    
    # Bonus 1: En Küçük Sayı
    en_kucuk = matris[0][0]
    for i in range(n):
        for j in range(n):
            if matris[i][j] < en_kucuk:
                en_kucuk = matris[i][j]
    print(f"\nMatrisin en küçük sayısı: {en_kucuk}")

    # Bonus 2: Sütun Toplamları
    for j in range(n):
        sutun_toplami = 0
        # Bu sefer dış döngü sütunları (j), iç döngü satırları (i) geziyor
        for i in range(n):
            sutun_toplami += matris[i][j]
        print(f"{j + 1}. sütun toplamı: {sutun_toplami}")

    # Bonus 3: Matrisi Ters Yazdırma
    print("\nTers Matris:\n")
    # İndeksleri n-1'den başlatıp 0'a kadar geriye doğru saydırıyoruz
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            print(matris[i][j], end=" ")
        print()

    # Bonus 4: Çift Sayıları Listeleme
    print("\nÇift sayılar:\n")
    cift_sayilar = []
    for i in range(n):
        for j in range(n):
            # 2'ye bölümünden kalan 0 ise sayıyı listeye ekle
            if matris[i][j] % 2 == 0:
                cift_sayilar.append(matris[i][j])
    
    # Listeyi aralarında boşluk olacak şekilde ekrana yazdırıyoruz
    print(" ".join(map(str, cift_sayilar)))

# Programı çalıştıran ana blok
if __name__ == "__main__":
    main()