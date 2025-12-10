
import json
import random
import os

def rastgele_vecize_getir():
    """
    data/vecizeler.json dosyasından rastgele bir vecize okur ve döner.
    """
    json_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "vecizeler.json")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            vecizeler = json.load(f)
            
        secilen = random.choice(vecizeler)
        return secilen
    except Exception as e:
        return {"soz": "Hata: Vecize veritabanı okunamadı.", "kaynak": str(e)}

if __name__ == "__main__":
    vecize = rastgele_vecize_getir()
    print("\n" + "=" * 50)
    print(f"\n🌟 \"{vecize['soz']}\"\n")
    print(f"                                   — {vecize['kaynak']}")
    print("\n" + "=" * 50 + "\n")
