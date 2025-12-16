# 📜 Risale-i Nur Külliyatı: Asa-yi Musa Code

![Asa-yi Musa Banner](assets/banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Asa-yi-Musa-Code/graphs/commit-activity)

## 🌟 Giriş: Asa-yi Musa Code Vizyonu

> "Vicdanın ziyası, ulûm-u diniyedir. Aklın nuru, fünun-u medeniyedir. İkisinin imtizacıyla hakikat tecelli eder." — *Münazarat*

Bu depo (**Repo**), Bediüzzaman Said Nursî'nin şaheseri **Risale-i Nur Külliyatı**'nı; **dijital analiz**, **yapay zeka**, **istatistiksel modelleme** ve **tematik haritalama** yöntemleriyle yeniden keşfetmek için tasarlanmış disiplinlerarası bir "Sanal Medrese" projesidir.

Amacımız, klasik metinleri modern zihnin idrakine sunmak ve Kuranî hakikatlerin dijital çağdaki yansımalarını araştırmaktır.

---

## 🏛️ Sanal Medrese: İçerik Haritası

Proje, Risale-i Nur'u sistematik bir şekilde incelemek için modüler bir yapı sunar. Aşağıdaki bağlantılardan ilgili çalışma alanlarına ulaşabilirsiniz.

### 📖 01. Temel Kavramlar ve Lügat
Risale-i Nur'un terminolojisine hakim olmak için başlangıç noktası.
- [Tevhid İspat Modeli](01-Temel-Kavramlar/Tevhid-İspat.md): Tevhid hakikatini ispatlayan mantıksal deliller.
- [Haşir ve Ahiret Sırları](01-Temel-Kavramlar/Haşir-ve-Ahiret-Sirlari.md): Öldükten sonra dirilişin akli temelleri.
- [Kader ve Cüz-i İrade Çözümlemesi](01-Temel-Kavramlar/Kader-ve-Cuz-i-Irade-Cozumlemesi.md): Kader probleminin sadeleştirilmiş analizi.

### 📚 02. Eser Özetleri ve Tematik İndeks
Külliyatın ana kitaplarının konsantre özetleri.
- [Sözler Tematik Özeti](02-Eser-Ozetleri/Sözler-Tematik-Ozeti.md): Sözler kitabındaki ana temaların dökümü.

### 🧠 03. Metodoloji ve Usul
Bediüzzaman'ın tefekkür sistemi ve ispat yöntemleri.
- [Temsil Metodu Nedir?](03-Metodoloji-ve-Usul/Temsil-Metodu-Nedir.md): Hakikatleri dürbün gibi yakınlaştıran hikayeler.
- [Kainatı Okuma Sanatı](03-Metodoloji-ve-Usul/Kainati-Okuma-Sanati.md): Mana-yı harfi ile kainata bakış.
- [Mantık Zincirleri](03-Metodoloji-ve-Usul/Mantık-Zincirleri.md): Külliyattaki akıl yürütme şemaları.

### 🌍 04. Modern Meseleler ve Cevaplar
Günümüzün felsefi ve sosyal sorularına Risale perspektifinden bakış.
- [Ruh ve Beden Münasebeti](04-Modern-Meseleler-Cevaplar/Ruh-ve-Beden-Munasebeti.md): Modern psikoloji ve Risale-i Nur.
- [Pozitivizm Eleştirisi](04-Modern-Meseleler-Cevaplar/Pozitivizm-Eleştirisi.md): Maddecilik yanılgısına cevaplar.
- [Felsefe ve Şeytan](04-Modern-Meseleler-Cevaplar/Felsefe-ve-Seytan.md): Şüphelerin kaynağı ve analizi.

### 🕯️ 05. Okuma Rehberi
Yeni başlayanlar ve derinleşmek isteyenler için yol haritaları.
- [Seviye 1: Başlangıç](05-Okuma-Rehberi/Seviye-1.md) | [Seviye 2: Orta](05-Okuma-Rehberi/Seviye-2.md) | [Seviye 3: İleri](05-Okuma-Rehberi/Seviye-3.md)

### 🕰️ 06. Biyografi ve Tarihçe-i Hayat
Müellifin hayatının devreleri.
- [Eski Said Dönemi](06-Biyografi-ve-Tarih/Eski-Said-Donemi.md)
- [Yeni Said Dönemi](06-Biyografi-ve-Tarih/Yeni-Said-Donemi.md)
- [Üçüncü Said Dönemi](06-Biyografi-ve-Tarih/Ucuncu-Said-Donemi.md)

---

## 🛠️ Teknik Altyapı ve Araçlar (Toolkit)

Bu proje sadece metinlerden ibaret değildir; aynı zamanda bu metinleri analiz etmek için geliştirilmiş Python araçları içerir.

### 📂 `src/` - Kaynak Kodlar
- **`app.py`**: Streamlit tabanlı web arayüzü. Külliyat üzerinde interaktif analizler yapmanızı sağlar.
- **`nur_cli.py`**: Komut satırı (CLI) üzerinden hızlı işlemler (ebced, arama, vecize) yapmak için araç.
- **`ebced_hesaplayici.py`**: Osmanlıca/Arapça metinlerin Ebced değerini hesaplayan modül.
- **`nurlib/` Paketi**:
    - `analiz.py`: Kelime frekansı, kök bulma ve metin madenciliği fonksiyonları.
    - `cifir.py`: Cifir hesaplamaları için çekirdek algoritmalar.

### 📂 `data/` - Veri Setleri
- Projenin analizlerinde kullanılan ham ve işlenmiş metin verileri, JSON formatındaki vecizeler ve lügatçeler burada saklanır.

---

## 🚀 Hızlı Başlangıç (Quick Start)

### Kurulum

1.  Repoyu klonlayın:
    ```bash
    git clone https://github.com/bahattinyunus/Asa-yi-Musa-Code.git
    cd Asa-yi-Musa-Code
    ```

2.  Gerekli paketleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

### Çalıştırma

**Web Arayüzü (Önerilen):**
```bash
streamlit run app.py
```

**CLI Aracı:**
```bash
python src/nur_cli.py --help
```

---

## 🤝 Katkıda Bulunma

Bu depo, kolektif bir tefekkür projesidir. Hataları düzeltmek, yeni analiz modülleri eklemek veya içerik zenginleştirmek için katkılarınızı bekliyoruz! Lütfen detaylar için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını inceleyin.

---

**"Sözler, şüpheleri izale etmek içindir; Asa-yi Musa ise firavunlaşmış enaniyetleri kırmak içindir."**
