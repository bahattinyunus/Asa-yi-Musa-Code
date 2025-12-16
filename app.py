import streamlit as st
import pandas as pd
import altair as alt
from src.nurlib import ebced_hesapla, rastgele_vecize_getir, kelime_frekansi_hesapla

# Sayfa Ayarları
st.set_page_config(
    page_title="Asa-yi Musa Code",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Harici Stil (CSS) - "WOW" etkisi için
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        color: white;
        background: linear-gradient(45deg, #11998e, #38ef7d);
        border: none;
        border-radius: 20px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: 300;
        color: #555;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Kenar Çubuğu
with st.sidebar:
    st.image("assets/banner.png", use_container_width=True)
    st.title("Gezinti")
    page = st.radio("Bölümler", ["Ana Sayfa", "Ebced Hesaplayıcı", "Tefekkür (Vecize)", "Kelime Analizi"])
    st.markdown("---")
    st.info("Bu proje Risale-i Nur Külliyatı'nı dijital araçlarla keşfetmek için tasarlanmıştır.")

# Sayfa Yönlendirme
if page == "Ana Sayfa":
    st.title("Hoş Geldiniz: Asa-yi Musa Code")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔍 Projenin Amacı</h3>
        <p class="big-font">
        Bu depo, Bediüzzaman Said Nursî tarafından kaleme alınan Risale-i Nur Külliyatı'nı, 
        modern dünyanın entelektüel ve manevi ihtiyaçlarına cevap verecek şekilde, 
        analitik ve teknolojik bir çerçevede incelemek üzere tasarlanmıştır.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📂 Keşfedebileceğiniz İçerikler")
        c1, c2, c3 = st.columns(3)
        c1.metric("Temel Kavramlar", "10+", "Md Dosyası")
        c2.metric("Eser Özetleri", "4", "Ana Kitap")
        c3.metric("Dijital Araçlar", "3", "Aktif Modül")

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🚀 Nasıl Başlarım?</h4>
        <ol>
        <li>Soldaki menüden bir araç seçin.</li>
        <li><b>Ebced</b> ile metinlerin sayısal değerine bakın.</li>
        <li><b>Tefekkür</b> ile günün sözünü alın.</li>
        <li><b>Analiz</b> ile külliyatın haritasını görün.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

elif page == "Ebced Hesaplayıcı":
    st.title("🧮 Ebced Hesaplayıcı")
    st.markdown("Cifir ilmi yaklaşımıyla metinlerin sayısal değerini hesaplayın.")
    
    metin = st.text_area("Metni Giriniz:", height=150, placeholder="Örn: Bismillah her hayrın başıdır...")
    
    if metin:
        toplam, detaylar = ebced_hesapla(metin)
        
        st.metric(label="Toplam Ebced Değeri", value=toplam)
        
        with st.expander("Harf Harf Detaylar"):
            st.write(" + ".join(detaylar))
            
elif page == "Tefekkür (Vecize)":
    st.title("🌟 Tefekkür Köşesi")
    
    if st.button("Yeni Bir Vecize Getir"):
        vecize = rastgele_vecize_getir()
        st.session_state['vecize'] = vecize
    
    if 'vecize' not in st.session_state:
        st.session_state['vecize'] = rastgele_vecize_getir()
        
    v = st.session_state['vecize']
    
    st.markdown(f"""
    <div class="main">
        <br>
        <div style="text-align: center; padding: 40px; background-color: #fff; border-left: 5px solid #11998e; border-radius: 5px; box-shadow: 0 2px 4px #eee;">
            <h2 style="color: #333; font-style: italic;">"{v['soz']}"</h2>
            <hr style="width: 50%; margin: 20px auto; border-top: 1px dashed #ccc;">
            <h4 style="color: #11998e;">— {v['kaynak']}</h4>
        </div>
        <br>
    </div>
    """, unsafe_allow_html=True)

elif page == "Kelime Analizi":
    st.title("📊 Kelime Frekansı Analizi")
    st.markdown("Repo içindeki metinlerde en sık geçen kelimelerin analizi.")
    
    limit = st.slider("Kelime Sayısı", 5, 50, 15)
    
    if st.button("Analizi Başlat"):
        with st.spinner("Dosyalar taranıyor..."):
            veriler = kelime_frekansi_hesapla(top_n=limit)
            
        df = pd.DataFrame(veriler, columns=["Kelime", "Frekans"])
        
        st.subheader(f"En Sık Kullanılan {limit} Kelime")
        
        # Altair Chart
        c = alt.Chart(df).mark_bar().encode(
            x=alt.X('Kelime', sort=None),
            y='Frekans',
            color=alt.Color('Frekans', scale=alt.Scale(scheme='tealblues')),
            tooltip=['Kelime', 'Frekans']
        ).properties(height=400)
        
        st.altair_chart(c, use_container_width=True)
        
        with st.expander("Veri Tablosunu Gör"):
            st.dataframe(df)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: #aaa; font-size: 12px;'>Asa-yi Musa Code &copy; 2025 - Made with ❤️ by Deepmind</div>", unsafe_allow_html=True)
