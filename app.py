import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK İş Yönetim Sistemi",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="collapsed" # Mobilde alanı genişletmek için kapalı başlar
)

# --- OTURUM YÖNETİMİ ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# --- MOBİL UYUMLU RESPONSIVE TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Temel Responsive Ayarlar */
    .stApp { background-color: #f0f2f5; color: #1e1e1e; }
    
    /* Haber Bandı - Mobilde Yazı Boyutu Ayarı */
    .ticker-wrap {
        width: 100%; overflow: hidden; background: #ffffff; 
        color: #e30613; padding: 10px 0; border-radius: 8px; 
        margin-bottom: 15px; border: 1px solid #e0e0e0;
        font-size: 14px;
    }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 30s linear infinite; }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Header - Mobilde Dikey Hizalama */
    .header-container {
        display: flex; align-items: center; background: #ffffff; 
        padding: 15px; border-radius: 12px; border-top: 5px solid #e30613;
        margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        flex-wrap: wrap; justify-content: center; text-align: center;
    }
    .system-title { font-size: clamp(18px, 4vw, 24px); font-weight: 800; color: #333; margin: 10px; }

    /* Kartlar - Dokunmatik Dostu */
    .action-card {
        background: #ffffff; padding: 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; margin-bottom: 15px; 
    }
    .action-card h3 { color: #e30613; font-size: 18px; margin-bottom: 12px; }

    /* Dijital Göstergeler - Mobilde 2'li Izgara */
    .stat-card {
        background: #ffffff; padding: 15px; border-radius: 10px;
        text-align: center; border-bottom: 3px solid #e30613;
        margin-bottom: 10px;
    }
    .stat-val { font-size: 24px; font-weight: 800; color: #e30613; }
    
    /* Takvim - Küçük Ekranlarda Scroll Desteği */
    .cal-container { overflow-x: auto; }
    .cal-day { min-height: 80px; background: #ffffff; border-radius: 8px; padding: 5px; border: 1px solid #eee; font-size: 12px; }
    
    /* Buton Genişlikleri */
    div.stButton > button { width: 100% !important; border-radius: 8px; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST HABER BANDI ---
st.markdown('<div class="ticker-wrap"><div class="ticker">📢 ACİL: CİMER Yanıt Süresi Doluyor | 📱 SOSYAL MEDYA: Yeni Tasarımlar Yüklendi | ✅ TAMAMLANDI: Aylık Rapor Arşivlendi</div></div>', unsafe_allow_html=True)

# --- ÜST PANEL ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/tr/b/b2/T%C3%BCrk_Akreditasyon_Kurumu_logosu.png" width="80">
        <div class="system-title">TÜRKAK İş Yönetim Sistemi</div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 📋 MENÜ")
    menu = st.radio("", ["🏠 Dashboard", "📱 Sosyal Medya", "📄 Yazışmalar", "🏛️ CİMER", "🎨 Tasarım", "🛒 Satın Alma"])
    st.divider()
    if st.session_state.logged_in:
        st.success(f"👤 {st.session_state.user_name}")
        if st.button("Güvenli Çıkış"):
            st.session_state.logged_in = False
            st.rerun()

# --- ANA İÇERİK ---
if menu == "🏠 Dashboard":
    # İstatistikler - Mobilde 2x2 düzeni için columns kullanımı
    m1, m2 = st.columns(2)
    m1.markdown('<div class="stat-card"><div class="stat-val">12</div><div style="font-size:12px;">Bekleyen İş</div></div>', unsafe_allow_html=True)
    m2.markdown('<div class="stat-card"><div class="stat-val">04</div><div style="font-size:12px;">Acil Görev</div></div>', unsafe_allow_html=True)
    
    m3, m4 = st.columns(2)
    m3.markdown('<div class="stat-card"><div class="stat-val">%62</div><div style="font-size:12px;">Bütçe</div></div>', unsafe_allow_html=True)
    m4.markdown('<div class="stat-card"><div class="stat-val">4.8</div><div style="font-size:12px;">CİMER</div></div>', unsafe_allow_html=True)

    # Takvim ve Formlar (Mobilde Alt Alta Gelir)
    col_main, col_right = st.columns([2, 1])

    with col_main:
        st.subheader("🗓️ Ajanda")
        with st.container():
            cal_data = cal.monthcalendar(2026, 5)
            # Mobilde takvim sütunlarını daraltıyoruz
            d_cols = st.columns(7)
            days = ["P", "S", "Ç", "P", "C", "C", "P"]
            for i, d in enumerate(days): d_cols[i].caption(f"**{d}**")
            
            for week in cal_data:
                w_cols = st.columns(7)
                for i, day in enumerate(week):
                    if day != 0:
                        with w_cols[i]:
                            st.markdown(f'<div class="cal-day"><b style="color:#e30613;">{day}</b></div>', unsafe_allow_html=True)

    with col_right:
        # Üye Girişi
        st.markdown('<div class="action-card"><h3>👤 Ekip Girişi</h3>', unsafe_allow_html=True)
        if not st.session_state.logged_in:
            u = st.text_input("Kullanıcı", key="user_idx")
            p = st.text_input("Şifre", type="password", key="pass_idx")
            if st.button("Bağlan"):
                if u == "turkak" and p == "1234":
                    st.session_state.logged_in = True
                    st.session_state.user_name = u
                    st.rerun()
                else:
                    st.error("Hata!")
        else:
            st.info(f"Hoş geldin, {st.session_state.user_name}")
        st.markdown('</div>', unsafe_allow_html=True)

        # İş Girişi
        st.markdown('<div class="action-card"><h3>➕ Yeni İş</h3>', unsafe_allow_html=True)
        if st.session_state.logged_in:
            st.text_input("Başlık")
            st.selectbox("Modül", ["Tasarım", "Yazışma", "Sosyal Medya"])
            st.button("Kaydet")
        else:
            st.warning("Giriş yapın.")
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.title(menu)
    st.info("Bu modül mobil görünüm için optimize edilmiştir.")
