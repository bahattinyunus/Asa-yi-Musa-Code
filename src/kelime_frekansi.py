
import os
import re
from collections import Counter

def kelime_frekansi_analizi(kok_dizin):
    """
    Belirtilen dizindeki tüm Markdown dosyalarını tarar ve en sık kullanılan kelimeleri bulur.
    """
    tum_metin = ""
    md_dosyalari = []
    
    # Dizini tara
    for root, dirs, files in os.walk(kok_dizin):
        for file in files:
            if file.endswith(".md"):
                dosya_yolu = os.path.join(root, file)
                md_dosyalari.append(dosya_yolu)
                with open(dosya_yolu, "r", encoding="utf-8") as f:
                    tum_metin += " " + f.read()
    
    # Temizlik
    tum_metin = tum_metin.lower()
    # Sadece harfleri al
    kelimeler = re.findall(r'\b\w+\b', tum_metin)
    
    # Etkisiz kelimeleri (Stop words) çıkar
    etkisiz_kelimeler = {
        've', 'bir', 'bu', 'da', 'de', 'ile', 'için', 'o', 'ne', 'gibi', 'en', 'çok', 'her', 'ama', 'fakat', 
        'olan', 'olarak', 'ise', 'ki', 'daha', 'var', 'yok', 'mı', 'mi', 'mu', 'mü', 'ben', 'sen', 'biz', 'siz',
        'onlar', 'bunu', 'şunu', 'bunun', 'şunun', 'dedi', 'diye', 'etmek', 'olmak', 'kadar', 'tarafından'
    }
    
    anlamli_kelimeler = [k for k in kelimeler if k not in etkisiz_kelimeler and len(k) > 2]
    
    # Sayma
    sayac = Counter(anlamli_kelimeler)
    en_sik = sayac.most_common(20)
    
    return len(md_dosyalari), len(kelimeler), en_sik

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Proje kök dizini
    
    print(f"Analyzing directory: {current_dir}...")
    dosya_sayisi, kelime_sayisi, en_sik = kelime_frekansi_analizi(current_dir)
    
    print(f"\n--- Analiz Sonuçları ---")
    print(f"Taranan Markdown Dosyası: {dosya_sayisi}")
    print(f"Toplam Kelime Sayısı: {kelime_sayisi}")
    print("\nEn Sık Kullanılan 20 Kavram:")
    print("-" * 30)
    for kelime, sayi in en_sik:
        print(f"{kelime.ljust(15)}: {sayi}")
