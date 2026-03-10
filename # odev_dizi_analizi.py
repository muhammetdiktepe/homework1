# odev_dizi_analizi.py
# Veri Yapıları ve Algoritmalar - Dizi Analizi Programı

def main():
    # ==========================================
    # BÖLÜM 1: Kullanıcıdan Veri Alma
    # ==========================================
    n = int(input("Kaç sayı gireceksiniz: "))
    dizi = []

    # Kullanıcının girdiği n adet sayıyı listeye ekliyoruz
    for i in range(n):
        sayi = int(input(f"Sayı {i + 1}: "))
        dizi.append(sayi)

    # Eğer kullanıcı 0 girerse programın hata vermemesi için basit bir kontrol
    if n <= 0:
        print("İşlem yapılacak sayı yok.")
        return

    # ==========================================
    # BÖLÜM 2: Dizi Analizi
    # ==========================================
    toplam = 0
    en_buyuk = dizi[0] # İlk elemanı geçici olarak en büyük kabul ediyoruz
    en_kucuk = dizi[0] # İlk elemanı geçici olarak en küçük kabul ediyoruz

    # Dizinin elemanlarını tek tek geziyoruz
    for sayi in dizi:
        toplam += sayi  # Toplama ekle
        
        if sayi > en_buyuk:
            en_buyuk = sayi  # Yeni bir en büyük bulursak güncelle
            
        if sayi < en_kucuk:
            en_kucuk = sayi  # Yeni bir en küçük bulursak güncelle

    ortalama = toplam / n

    print("\n" + "-"*30)
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama}")
    print(f"En büyük sayı: {en_buyuk}")
    print(f"En küçük sayı: {en_kucuk}")

    # ==========================================
    # BÖLÜM 3: Özel Analiz
    # ==========================================
    cift_sayisi = 0
    tek_sayisi = 0
    ondan_buyuk_sayisi = 0

    for sayi in dizi:
        if sayi % 2 == 0:
            cift_sayisi += 1
        else:
            tek_sayisi += 1

        if sayi > 10:
            ondan_buyuk_sayisi += 1

    print("-" * 30)
    print(f"Çift sayı sayısı: {cift_sayisi}")
    print(f"Tek sayı sayısı: {tek_sayisi}")
    print(f"10'dan büyük sayı sayısı: {ondan_buyuk_sayisi}")

    # ==========================================
    # BÖLÜM 4: Diziyi Ters Yazdırma
    # ==========================================
    print("-" * 30)
    print(f"Orijinal dizi: {dizi}\n")
    print("Ters dizi:")
    
    # İndeksleri n-1'den başlatıp 0'a doğru geriye saydırıyoruz
    for i in range(n - 1, -1, -1):
        print(dizi[i], end=" ")
    print() # Alt satıra geçmek için boş print

    # ==========================================
    # BÖLÜM 5: Sayı Arama
    # ==========================================
    print("-" * 30)
    aranan = int(input("Aranacak sayı: "))
    bulundu_mu = False

    for sayi in dizi:
        if sayi == aranan:
            bulundu_mu = True
            break # Sayıyı bulduysak döngüyü daha fazla yormaya gerek yok

    if bulundu_mu:
        print("Sayı dizide bulundu")
    else:
        print("Sayı dizide bulunamadı")

    # ==========================================
    # BONUS BÖLÜM (İsteğe Bağlı Özellikler)
    # ==========================================
    print("\n" + "="*30)
    print("BONUS ANALİZLER")
    print("="*30)

    # 1. Negatif Sayıları Listeleme
    negatifler = []
    for sayi in dizi:
        if sayi < 0:
            negatifler.append(sayi)
    
    if negatifler:
        print(f"Negatif sayılar: {negatifler}")
    else:
        print("Dizide negatif sayı yok.")

    # 2. Ortalamanın Üzerindeki Sayıları Yazdırma
    ortalamadan_buyukler = []
    for sayi in dizi:
        if sayi > ortalama:
            ortalamadan_buyukler.append(sayi)
    print(f"Ortalamanın üzerindeki sayılar: {ortalamadan_buyukler}")

    # 3. En Çok Tekrar Eden Sayıyı Bulma
    en_cok_tekrar_eden = dizi[0]
    maksimum_tekrar = 0

    for sayi in dizi:
        # Listenin .count() metodu o sayının dizide kaç kez geçtiğini sayar
        tekrar_sayisi = dizi.count(sayi) 
        if tekrar_sayisi > maksimum_tekrar:
            maksimum_tekrar = tekrar_sayisi
            en_cok_tekrar_eden = sayi

    if maksimum_tekrar > 1:
        print(f"En çok tekrar eden sayı: {en_cok_tekrar_eden} ({maksimum_tekrar} kez tekrar etti)")
    else:
        print("Dizide tekrar eden sayı bulunmuyor (Tüm sayılar benzersiz).")


if __name__ == "__main__":
    main()