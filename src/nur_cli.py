import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from nurlib import ebced_hesapla, rastgele_vecize_getir, kelime_frekansi_hesapla

app = typer.Typer(help="Asa-yi Musa Code - Dijital Tefekkür Aracı")
console = Console()

@app.command()
def intro():
    """
    Proje hakkında bilgi verir.
    """
    console.print(Panel.fit("[bold green]Asa-yi Musa Code[/bold green]\n\nRisale-i Nur Külliyatı'nı dijital araçlarla keşfetmek için tasarlanmıştır.", border_style="green"))

@app.command()
def ebced(metin: str):
    """
    Verilen metnin Ebced değerini hesaplar.
    """
    toplam, detaylar = ebced_hesapla(metin)
    
    table = Table(title=f"Ebced Analizi: {metin}")
    table.add_column("Harf", justify="center", style="cyan", no_wrap=True)
    table.add_column("Değer", justify="right", style="magenta")

    for detay in detaylar:
        h, d = detay.split(": ")
        table.add_row(h, d)
        
    console.print(table)
    console.print(f"\n[bold yellow]Toplam Ebced Değeri:[/bold yellow] [bold white]{toplam}[/bold white]\n")

@app.command()
def vecize():
    """
    Rastgele bir vecize getirir.
    """
    v = rastgele_vecize_getir()
    if "soz" in v:
        text = f"[italic]\"{v['soz']}\"[/italic]\n\n[bold right]— {v['kaynak']}[/bold right]"
        console.print(Panel(text, title="Günün Vecizesi", border_style="blue"))
    else:
        console.print("[bold red]Hata:[/bold red] Vecize getirilemedi.")

@app.command()
def frekans(limit: int = 10):
    """
    Külliyattaki en sık kullanılan kelimeleri listeler.
    """
    console.print("[dim]Dosyalar taranıyor, lütfen bekleyin...[/dim]")
    sonuclar = kelime_frekansi_hesapla(top_n=limit)
    
    table = Table(title=f"Kelime Frekansı (İlk {limit})")
    table.add_column("Sıra", justify="right", style="dim")
    table.add_column("Kelime", style="green")
    table.add_column("Tekrar", justify="right", style="bold magenta")
    
    for i, (kelime, sayi) in enumerate(sonuclar, 1):
        table.add_row(str(i), kelime, str(sayi))
        
    console.print(table)

if __name__ == "__main__":
    app()
