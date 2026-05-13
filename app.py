import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal
import os

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK İş Yönetim Sistemi",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- KURUMSAL TEMA VE MODERN TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Ana Arkaplan ve Font */
    .stApp { background-color: #f8f9fa; }
    
    /* Header Tasarımı */
    .header-container {
        display: flex; align-items: center; 
        background: white; padding: 15px 25px; 
        border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 30px; border-top: 4px solid #e30613;
    }
    .header-text {
        margin-left: 25px; color: #333;
        font-family: 'Inter', sans-serif;
    }
    .system-name { font-size: 26px; font-weight: 800; color: #e30613; line-height: 1.2; }
    .department-name { font-size: 16px; font-weight: 500; color: #666; }

    /* Kartlar ve Widgetlar */
    .metric-card {
        background: white; padding: 20px; border-radius: 12px;
        border-bottom: 3px solid #e30613; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    
    /* Takvim Stili */
    .cal-day-box {
        min-height: 120px; background: white; border-radius: 10px;
        padding: 10px; border: 1px solid #eee; transition: 0.3s;
    }
    .cal-day-box:hover { box-shadow: 0 5px 15px rgba(227, 6, 19, 0.1); border-color: #e30613; }
    .day-header { font-weight: 700; color: #e30613; margin-bottom: 8px; font-size: 18px; }
    
    /* Alarm ve Etiketler */
    .pulse-alarm {
        background: #e30613; color: white; padding: 12px;
        border-radius: 10px; text-align: center; font-weight: bold;
        animation: pulse-red 2s infinite;
    }
    @keyframes pulse-red { 0% {box-shadow: 0 0 0 0 rgba(227, 6, 19, 0.7);} 70% {box-shadow: 0 0 0 10px rgba(227, 6, 19, 0);} 100% {box-shadow: 0 0 0 0 rgba(227, 6, 19, 0);} }
    
    .event-label {
        font-size: 11px; padding: 3px 7px; border-radius: 5px; 
        color: white; margin-bottom: 4px; font-weight: 600;
        display: block; width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST PANEL (LOGO & BAŞLIK) ---
# logo.svg dosyasını yerel olarak kontrol et, yoksa placeholder koy
logo_path = "logo.svg"
col_header_1, col_header_2 = st.columns([1, 10])

with st.container():
    st.markdown(f"""
        <div class="header-container">
            <img src="https://raw.githubusercontent.com/yusuf-metin/streamlit-test/main/logo.png" width="90"> <!-- Yedek URL, logo.svg deponda olmalı -->
            <div class="header-text">
                <div class="system-name">İş Yönetim Sistemi</div>
                <div class="department-name">TÜRKAK Kurumsal İletişim Müdürlüğü</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 📊 Yönetim Paneli")
    main_menu = st.selectbox("Modül Seçiniz", [
        "🏠 Dashboard & Takvim",
        "📱 Sosyal Medya",
        "📄 Resmi Yazışmalar",
        "⚖️ Şikayet / İtiraz",
        "🏛️ CİMER / İleti",
        "🎨 Tasarım Faaliyetleri",
        "📅 Etkinlik Organizasyonu",
        "📧 E-Bülten",
        "💼 Özel Kalem & Bütçe",
        "🛒 Satın Alma"
    ])
    st.divider()
    st.write(f"📅 **Bugün:** {datetime.now().strftime('%d %B %Y')}")
    st.caption("v2.0 Production Ready")

# --- DATA (ÖRNEK İŞLER) ---
work_data = [
    {"gün": 14, "is": "LinkedIn Bülten", "renk": "#0077b5"},
    {"gün": 15, "is": "CİMER Yanıt", "renk": "#e30613"},
    {"gün": 18, "is": "Video Kurgu V1", "renk": "#333"}
]

# --- 1. DASHBOARD & FULL CALENDAR ---
if main_menu == "🏠 Dashboard & Takvim":
    c1, c2 = st.columns([3, 1])

    with c1:
        st.markdown("### 🗓️ Kurumsal Planlama Takvimi")
        
        # Takvim Grid Sistemi
        cal_data = cal.monthcalendar(2026, 5)
        days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        
        t_cols = st.columns(7)
        for idx, day_name in enumerate(days):
            t_cols[idx].markdown(f"<p style='text-align:center; font-weight:bold; color:#666;'>{day_name}</p>", unsafe_allow_html=True)

        for week in cal_data:
            w_cols = st.columns(7)
            for idx, day_num in enumerate(week):
                if day_num != 0:
                    with w_cols[idx]:
                        st.markdown(f'<div class="cal-day-box"><div class="day-header">{day_num}</div>', unsafe_allow_html=True)
                        # O güne ait görevleri listele
                        day_tasks = [t for t in work_data if t["gün"] == day_num]
                        for task in day_tasks:
                            st.markdown(f'<div class="event-label" style="background:{task["renk"]}">{task["is"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="pulse-alarm">🚨 ACİL AKSİYONLAR</div>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("""
            <div class="metric-card">
                <b>📌 Günün İşleri</b><br>
                <small>• BlueSky Post Planı<br>• Tasarım Revizeleri</small>
            </div><br>
            <div class="metric-card">
                <b>⏳ Bekleyen Onaylar</b><br>
                <small>• Satın Alma #12<br>• E-Bülten V2</small>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("➕ Hızlı Görev Tanımla"):
            st.text_input("Görev Adı")
            st.date_input("Tarih")
            st.button("Sisteme Kaydet")

# --- MODÜL İÇERİKLERİ (TASLAK) ---
elif main_menu == "📱 Sosyal Medya":
    st.subheader("Sosyal Medya Yönetimi")
    tab1, tab2 = st.tabs(["Yayın Takvimi", "Performans"])
    with tab1:
        st.info("BlueSky, Instagram, X ve LinkedIn içerikleri burada yönetilir.")
        st.button("Yeni İçerik Talebi Oluştur")

elif main_menu == "💼 Özel Kalem & Bütçe":
    st.subheader("Bütçe ve Harcama Takibi")
    m_col1, m_col2 = st.columns(2)
    m_col1.metric("Kullanılan Bütçe", "₺24.000")
    m_col2.metric("Kalan Limit", "₺176.000")

else:
    st.subheader(main_menu)
    st.write("Bu bölüm içerik girişi için hazırdır.")
