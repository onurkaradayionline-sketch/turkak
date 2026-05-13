import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK İş Yönetim Sistemi",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN KURUMSAL DİJİTAL TASARIM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;700&display=swap');
    
    .stApp { background-color: #0e1117; color: #ffffff; } /* Dark Mode Dijital Görünüm */
    
    /* Üst Haber Bandı (Kayar Yazı) */
    .ticker-wrap {
        width: 100%; overflow: hidden; background: #e30613; 
        color: white; padding: 10px 0; border-radius: 5px; margin-bottom: 20px;
    }
    .ticker {
        display: inline-block; white-space: nowrap; padding-right: 100%;
        animation: ticker 30s linear infinite; font-weight: bold;
    }
    @keyframes ticker {
        0% { transform: translate3d(0, 0, 0); }
        100% { transform: translate3d(-100%, 0, 0); }
    }

    /* Header Tasarımı */
    .header-container {
        display: flex; align-items: center; background: #1a1c24; 
        padding: 20px; border-radius: 15px; border-left: 10px solid #e30613;
        margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .system-name { font-family: 'Orbitron', sans-serif; font-size: 28px; color: #e30613; letter-spacing: 2px; }

    /* Dijital Kartlar */
    .digital-card {
        background: #1a1c24; padding: 20px; border-radius: 15px;
        border: 1px solid #333; text-align: center;
        transition: 0.3s;
    }
    .digital-card:hover { border-color: #e30613; box-shadow: 0 0 20px rgba(227, 6, 19, 0.2); }
    .digital-val { font-family: 'Orbitron', sans-serif; font-size: 32px; color: #e30613; }

    /* Takvim */
    .cal-box {
        min-height: 100px; background: #262730; border-radius: 10px;
        padding: 8px; border: 1px solid #444; margin-bottom: 5px;
    }
    .day-num { color: #e30613; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# --- KAYAR YAZI BANDI ---
st.markdown("""
    <div class="ticker-wrap">
        <div class="ticker">
            🚨 ACİL: CİMER Yanıt Süresi Doluyor (2 Gün) | 📢 YENİ: Sosyal Medya Haftalık Planı Girildi | 
            ✅ ONAYLANDI: Afiş Tasarımı Müdürlük Onayından Geçti | 🛠️ BEKLEMEDE: Satın Alma Talebi #442 
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ÜST PANEL (LOGO & BAŞLIK) ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    # Wikipedia üzerindeki logoyu referans alıyoruz (Daha güvenli erişim)
    st.image("https://upload.wikimedia.org/wikipedia/tr/b/b2/T%C3%BCrk_Akreditasyon_Kurumu_logosu.png", width=120)
with col_title:
    st.markdown('<div class="system-name">İş Yönetim Sistemi</div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#aaa;">TÜRKAK Kurumsal İletişim Müdürlüğü | Dijital Komuta Merkezi</div>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 📡 Sistem Modülleri")
    menu = st.selectbox("", ["🏠 Dashboard", "📱 Sosyal Medya", "📄 Yazışmalar", "🎨 Tasarım", "🛒 Satın Alma"])
    st.divider()
    st.info("Sistem Durumu: Online 🟢")

# --- DASHBOARD İÇERİĞİ ---
if menu == "🏠 Dashboard":
    # DİJİTAL GRAFİK METRİKLERİ
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="digital-card">Bekleyen İş<br><span class="digital-val">14</span></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="digital-card">Acil İş<br><span class="digital-val">03</span></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="digital-card">Tamamlanan<br><span class="digital-val">42</span></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="digital-card">Bütçe Durumu<br><span class="digital-val">%68</span></div>', unsafe_allow_html=True)

    st.write("")
    
    col_main, col_forms = st.columns([2, 1])

    # TAKVİM ALANI
    with col_main:
        st.subheader("📅 Planlama Takvimi")
        cal_data = cal.monthcalendar(2026, 5)
        days_cols = st.columns(7)
        for i, d in enumerate(["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]): days_cols[i].caption(d)
        
        for week in cal_data:
            w_cols = st.columns(7)
            for i, day in enumerate(week):
                if day != 0:
                    with w_cols[i]:
                        st.markdown(f'<div class="cal-box"><span class="day-num">{day}</span></div>', unsafe_allow_html=True)

    # GİRİŞ FORMLARI
    with col_forms:
        with st.expander("👤 Üye Girişi", expanded=True):
            st.text_input("Kullanıcı")
            st.text_input("Şifre", type="password")
            st.button("Sisteme Bağlan", use_container_width=True)
        
        with st.expander("➕ Hızlı İş Girişi", expanded=True):
            st.text_input("Görev")
            st.selectbox("Bölüm", ["Sosyal Medya", "Yazışma", "Tasarım"])
            st.date_input("Tarih")
            st.button("Görev Oluştur", use_container_width=True)

else:
    st.title(menu)
    st.write("Veri girişi bekleniyor...")
