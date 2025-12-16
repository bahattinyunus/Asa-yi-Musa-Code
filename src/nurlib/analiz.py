import os
import re
from collections import Counter

def kelime_frekansi_hesapla(root_dir=None, top_n=20):
    """
    Repo içindeki .md dosyalarını tarar ve en sık kullanılan kelimeleri bulur.
    """
    if root_dir is None:
        # src/nurlib/analiz.py -> .../...
        base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        corpus_path = os.path.join(base, "data", "corpus")
        if os.path.exists(corpus_path):
            root_dir = corpus_path
        else:
            root_dir = base

    exclude_dirs = {'.git', '.github', 'assets', 'src', '.gemini'}
    kelimeler = []
    
    for root, dirs, files in os.walk(root_dir):
        # Dizinleri filtrele
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        # Basit temizlik
                        content = re.sub(r'[^\w\s]', '', content.lower())
                        words = content.split()
                        # Stop words (basitçe)
                        stop_words = {'ve', 'ile', 'bir', 'bu', 'da', 'de', 'ki', 'için', 'o', 'ne', 'en', 'daha'}
                        filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
                        kelimeler.extend(filtered_words)
                except Exception:
                    pass
                    
    counter = Counter(kelimeler)
    return counter.most_common(top_n)
