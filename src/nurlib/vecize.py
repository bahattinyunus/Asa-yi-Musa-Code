import json
import random
import os

def rastgele_vecize_getir():
    """
    data/vecizeler.json dosyasından rastgele bir vecize okur ve döner.
    """
    # Proje kök dizinini bulmaya çalışalım (src/nurlib/vecize.py -> .../...)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    json_path = os.path.join(base_dir, "data", "vecizeler.json")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            vecizeler = json.load(f)
            
        secilen = random.choice(vecizeler)
        return secilen
    except Exception as e:
        return {"soz": f"Hata: Vecize veritabanı okunamadı. ({json_path})", "kaynak": str(e)}
