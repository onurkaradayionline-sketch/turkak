import streamlit as st
import pandas as pd
from datetime import datetime

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK Kurumsal İletişim İş Takip",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS: Çeviri Hatalarını ve Stil Bozulmalarını Engelleme ---
st.markdown("""
    <style>
    /* Google Translate kaynaklı hataları minimize etmek için */
    .stApp { overflow: hidden; }
    .main-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #004a99;
        margin-bottom: 20px;
    }
    .alarm-red {
        background-color: #ff4b4b;
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.5; } }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: NAVİGASYON ---
with st.sidebar:
    st.image("https://www.turkak.org.tr/assets/images/logo.png", width=180)
    st.title("Sistem Menüsü")
    menu = st.selectbox(
        "Modül Seçiniz:",
        ["🏠 Dashboard", "📱 Sosyal Medya", "📄 Resmi Yazışmalar", "🎨 Tasarım & Video", "⚖️ CİMER / Şikayet", "💰 Bütçe & Satın Alma"]
    )
    st.info(f"Kullanıcı: TÜRKAK Ekibi\nTarih: {datetime.now().strftime('%d.%m.%Y')}")

# --- DASHBOARD ---
if menu == "🏠 Dashboard":
    st.title("🚀 Kurumsal İletişim Komuta Merkezi")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📅 Haftalık Planlama")
        # Örnek iş listesi
        data = {
            "Modül": ["Sosyal Medya", "Tasarım", "CİMER", "Bütçe"],
            "Görev": ["Haftalık Bülten Paylaşımı", "Akreditasyon Afişi", "Vatandaş Cevabı", "Kamera Alım Onayı"],
            "Sorumlu": ["Ayşe", "Mehmet", "Fatma", "Ali"],
            "Durum": ["✅ Tamamlandı", "🟡 Devam Ediyor", "🔴 Acil", "⌛ Beklemede"]
        }
        df = pd.DataFrame(data)
        st.table(df)

    with col2:
        st.markdown('<div class="alarm-red">🚨 GÜNÜN KRİTİK İŞLERİ</div>', unsafe_allow_html=True)
        st.write("")
        st.warning("**Süre Doluyor:** BlueSky İçerik Planı")
        st.error("**Onay Bekliyor:** Satın Alma Talebi #442")
        
        with st.expander("➕ Hızlı Görev Ekle"):
            task_name = st.text_input("Görev Adı")
            task_type = st.selectbox("Tür", ["İçerik", "Tasarım", "Yazışma"])
            if st.button("Sisteme İşle"):
                st.success(f"'{task_name}' başarıyla eklendi!")

# --- SOSYAL MEDYA ---
elif menu == "📱 Sosyal Medya":
    st.title("Sosyal Medya Yönetimi")
    p_tabs = st.tabs(["Takvim", "İçerik Havuzu", "Performans"])
    with p_tabs[0]:
        st.info("Platformlar: Instagram, X, LinkedIn, YouTube, BlueSky, Next Sosyal")
        st.write("Planlanan paylaşımlar burada listelenir.")

# --- TASARIM & VİDEO ---
elif menu == "🎨 Tasarım & Video":
    st.title("Tasarım ve Video Süreçleri")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.subheader("Yeni Tasarım Talebi")
        st.selectbox("Materyal", ["Afiş", "Banner", "Sunum", "E-Bülten"])
        st.date_input("Deadline")
    with col_t2:
        st.subheader("Video Kurgu Takibi")
        st.write("Revize Süreçleri:")
        st.checkbox("V1 Kurgu Hazır")
        st.checkbox("Müdür Onayı Bekliyor")

# --- BÜTÇE & SATIN ALMA ---
elif menu == "💰 Bütçe & Satın Alma":
    st.title("Özel Kalem & Satın Alma")
    m1, m2 = st.columns(2)
    m1.metric("Kullanılan Bütçe", "45.200 ₺", "1.200 ₺")
    m2.metric("Kalan Limit", "154.800 ₺", "-5%")
    st.divider()
    st.subheader("Satın Alma Talep Formu")
    st.text_input("Hizmet/Ürün")
    st.number_input("Tahmini Tutar", min_value=0)

# --- DİĞER MODÜLLER ---
else:
    st.title(menu)
    st.write("Bu modül yapılandırma aşamasındadır. Veri girişi yapabilirsiniz.")
