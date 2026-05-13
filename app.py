import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK İletişim Portalı",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN KURUMSAL UI (CSS CUSTOMIZATION) ---
st.markdown("""
    <style>
    /* Global Font ve Arkaplan */
    .stApp { background-color: #fcfdfe; }
    
    /* Üst Bar Tasarımı */
    .top-header {
        display: flex; align-items: center; padding: 10px 0px;
        border-bottom: 2px solid #004a99; margin-bottom: 25px;
    }
    .system-title {
        color: #004a99; font-size: 24px; font-weight: 800;
        margin-left: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Kart Tasarımları */
    .modern-card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #eef2f6;
        margin-bottom: 15px;
    }
    
    /* Alarm Kutusu */
    .critical-alarm {
        background: linear-gradient(45deg, #ff4b4b, #ff7675);
        color: white; padding: 15px; border-radius: 10px;
        text-align: center; font-weight: bold; font-size: 18px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        animation: pulse 2s infinite;
    }
    @keyframes pulse { 0% {transform: scale(1);} 50% {transform: scale(1.02);} 100% {transform: scale(1);} }

    /* Takvim Hücreleri */
    .cal-box {
        min-height: 110px; border: 1px solid #edf2f7;
        background: #ffffff; border-radius: 8px; padding: 8px;
        transition: all 0.3s;
    }
    .cal-box:hover { border-color: #004a99; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
    .day-num { font-weight: bold; color: #4a5568; margin-bottom: 5px; }
    .tag { font-size: 10px; padding: 2px 6px; border-radius: 4px; color: white; margin-bottom: 3px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER (LOGO & BAŞLIK) ---
st.markdown(f"""
    <div class="top-header">
        <img src="https://www.turkak.org.tr/assets/images/logo.png" width="120">
        <div class="system-title">Kurumsal İletişim Müdürlüğü İş Yönetim Sistemi</div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛠️ Modül Menüsü")
    menu = st.radio("", [
        "🏠 Dashboard / Takvim",
        "📱 Sosyal Medya",
        "📄 Resmi Yazışmalar",
        "⚖️ Şikayet & İtiraz",
        "🏛️ CİMER / İleti",
        "🎨 Tasarım Faaliyetleri",
        "📅 Etkinlik Organizasyonu",
        "📧 E-Bülten",
        "💼 Özel Kalem & Bütçe",
        "🛒 Satın Alma"
    ])
    st.divider()
    st.caption(f"TÜRKAK v1.5 | {datetime.now().strftime('%d.%m.%Y')}")

# --- TAKVİM VERİSİ ---
sample_tasks = [
    {"g": 14, "m": "SM", "t": "Insta Paylaşım", "c": "#E1306C"},
    {"g": 15, "m": "CİMER", "t": "Son Gün!", "c": "#FF4B4B"},
    {"g": 18, "m": "TSR", "t": "Afiş Teslim", "c": "#004a99"}
]

# --- 1. DASHBOARD & TAKVİM ---
if menu == "🏠 Dashboard / Takvim":
    left_col, right_col = st.columns([3, 1])

    with left_col:
        st.markdown("### 🗓️ Kurumsal Planlama Takvimi")
        
        # Takvim Oluşturma
        cal_obj = cal.monthcalendar(2026, 5)
        days = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
        
        cols = st.columns(7)
        for i, d in enumerate(days):
            cols[i].markdown(f"<div style='text-align:center; color:#718096; font-weight:bold;'>{d}</div>", unsafe_allow_html=True)

        for week in cal_obj:
            w_cols = st.columns(7)
            for i, day in enumerate(week):
                if day != 0:
                    with w_cols[i]:
                        st.markdown(f'<div class="cal-box"><div class="day-num">{day}</div>', unsafe_allow_html=True)
                        # O güne ait işler
                        day_tasks = [x for x in sample_tasks if x["g"] == day]
                        for task in day_tasks:
                            st.markdown(f'<div class="tag" style="background:{task["c"]}">{task["t"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="critical-alarm">🚨 KRİTİK UYARILAR</div>', unsafe_allow_html=True)
        st.write("")
        
        with st.container():
            st.markdown('<div class="modern-card"><b>📌 Günün İşleri</b><br><small>• Web Sitesi Güncelleme<br>• Sosyal Medya Planı</small></div>', unsafe_allow_html=True)
            st.markdown('<div class="modern-card"><b>⏳ Bekleyen Onaylar</b><br><small>• Video Revize (Müdür)<br>• Satın Alma #45</small></div>', unsafe_allow_html=True)
            st.markdown('<div class="modern-card"><b>🔥 Geciken İşler</b><br><small style="color:red;">• CİMER Başvuru #122</small></div>', unsafe_allow_html=True)
        
        with st.expander("➕ Hızlı Görev Tanımla"):
            st.text_input("Görev")
            st.selectbox("Modül", ["Tasarım", "Yazışma", "Duyuru"])
            st.button("Kaydet")

# --- MODÜLLERİN İÇERİĞİ ---
elif menu == "📱 Sosyal Medya":
    st.header("📱 Sosyal Medya Yönetimi")
    t1, t2, t3 = st.tabs(["Planlama", "İçerik Talebi", "Raporlar"])
    with t1:
        st.info("Instagram, X, LinkedIn, YouTube, BlueSky, Next Sosyal")
        st.data_editor(pd.DataFrame({
            "Platform": ["Instagram", "BlueSky", "LinkedIn"],
            "Konu": ["Akreditasyon", "Yeni Blog", "Etkinlik"],
            "Durum": ["Hazır", "Beklemede", "Onayda"]
        }))

elif menu == "📄 Resmi Yazışmalar":
    st.header("📄 Resmi Yazışma Yönetimi")
    c1, c2 = st.columns(2)
    c1.markdown('<div class="modern-card">📬 <b>Gelen Evrak</b><br>Takip No: 2026/45</div>', unsafe_allow_html=True)
    c2.markdown('<div class="modern-card">📤 <b>Giden Evrak</b><br>Arşiv No: 2026/88</div>', unsafe_allow_html=True)

# Diğer modüller için benzer tasarımları bu şekilde ekleyebilirsin...
else:
    st.header(menu)
    st.write(f"{menu} süreci için veriler buraya gelecek.")
