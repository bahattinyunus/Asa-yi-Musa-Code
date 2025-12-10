
def ebced_hesapla(metin):
    """
    Verilen metnin Ebced değerini hesaplar.
    Basit Ebced tablosu kullanılmıştır.
    """
    ebced_degerleri = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 8, 'g': 1000, 'ğ': 1000, 'h': 8, 'ı': 10, 'i': 10,
        'j': 3, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 6, 'ö': 6, 'p': 2, 'r': 200, 's': 60, 'ş': 300,
        't': 400, 'u': 6, 'ü': 6, 'v': 6, 'y': 10, 'z': 7,
        'ç': 3, # Jim gibi
        ' ': 0
    }
    
    # Osmanlıca harflerin tam karşılığı Latin alfabesinde %100 olmadığı için
    # bu popüler/yaklaşık bir eşleştirmedir.
    
    toplam = 0
    metin = metin.lower()
    
    detaylar = []
    
    for harf in metin:
        if harf in ebced_degerleri:
            deger = ebced_degerleri[harf]
            toplam += deger
            if deger > 0:
                detaylar.append(f"{harf}: {deger}")
                
    return toplam, detaylar

if __name__ == "__main__":
    print("--- Ebced Hesaplayıcı ---\n")
    print("Not: Bu hesaplama Latin harfleri üzerinden yapılan yaklaşık bir değerdir.")
    while True:
        giris = input("\nMetni giriniz (Çıkış için 'q'): ")
        if giris.lower() == 'q':
            break
            
        sonuc, detay = ebced_hesapla(giris)
        print(f"\n'{giris}' ifadesinin Ebced Değeri: {sonuc}")
        print(f"Detaylar: {' + '.join(detay)}")
