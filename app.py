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

# --- LOGO YÜKLEME FONKSİYONU ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

logo_base64 = get_base64_of_bin_file("logo.webp")
logo_html = f"data:image/webp;base64,{logo_base64}" if logo_base64 else ""

# --- MODERN KURUMSAL TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .header-container {
        display: flex; align-items: center; 
        background: white; padding: 15px 25px; 
        border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 25px; border-top: 5px solid #e30613;
    }
    .system-name { font-size: 24px; font-weight: 800; color: #e30613; margin-left: 20px; }
    .panel-card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px;
        border: 1px solid #eee;
    }
    .cal-box {
        min-height: 110px; background: white; border-radius: 10px;
        padding: 8px; border: 1px solid #eee; transition: 0.3s;
    }
    .cal-box:hover { border-color: #e30613; }
    .tag { font-size: 10px; padding: 2px 5px; border-radius: 4px; color: white; margin-bottom: 3px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST PANEL ---
st.markdown(f"""
    <div class="header-container">
        <img src="{logo_html}" width="80" alt="LOGO">
        <div>
            <div class="system-name">İş Yönetim Sistemi</div>
            <div style="margin-left:20px; color:#666; font-weight:500;">TÜRKAK Kurumsal İletişim Müdürlüğü</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🏢 Kurumsal Menü")
    main_menu = st.selectbox("Gitmek İstediğiniz Modül", [
        "🏠 Dashboard / Takvim", "📱 Sosyal Medya", "📄 Resmi Yazışmalar", 
        "⚖️ Şikayet / İtiraz", "🏛️ CİMER / İleti", "🎨 Tasarım Faaliyetleri", 
        "📅 Etkinlik", "📧 E-Bülten", "💼 Bütçe", "🛒 Satın Alma"
    ])
    st.divider()
    st.caption(f"v2.2 | {datetime.now().strftime('%d.%m.%Y')}")

# --- ANA SAYFA AKIŞI ---
if main_menu == "🏠 Dashboard / Takvim":
    col_takvim, col_islem = st.columns([2.5, 1])

    # SOL TARAF: TAKVİM
    with col_takvim:
        st.markdown("### 🗓️ Kurumsal Planlama Takvimi")
        cal_data = cal.monthcalendar(2026, 5)
        days = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
        t_cols = st.columns(7)
        for i, d in enumerate(days): t_cols[i].markdown(f"<p style='text-align:center; font-weight:bold;'>{d}</p>", unsafe_allow_html=True)

        for week in cal_data:
            w_cols = st.columns(7)
            for i, day in enumerate(week):
                if day != 0:
                    with w_cols[i]:
                        st.markdown(f'<div class="cal-box"><div style="color:#e30613; font-weight:bold;">{day}</div>', unsafe_allow_html=True)
                        # Örnek statik işler
                        if day == 14: st.markdown('<div class="tag" style="background:#0077b5;">LinkedIn Post</div>', unsafe_allow_html=True)
                        if day == 15: st.markdown('<div class="tag" style="background:#e30613;">CİMER Yanıt</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

    # SAĞ TARAF: ÜYE GİRİŞİ & İŞ GİRİŞİ
    with col_islem:
        # 1. Üye Girişi Bölümü
        with st.container():
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            st.subheader("👤 Ekip Girişi")
            with st.form("login_form"):
                user = st.text_input("Kullanıcı Adı")
                pw = st.text_input("Şifre", type="password")
                if st.form_submit_button("Giriş Yap"):
                    st.success(f"Hoş geldin, {user}!")
            st.markdown('</div>', unsafe_allow_html=True)

        # 2. İş Giriş Bölümü
        with st.container():
            st.markdown('<div class="panel-card">', unsafe_allow_html=True)
            st.subheader("➕ Yeni İş Girişi")
            with st.form("task_entry"):
                task_name = st.text_input("İşin Tanımı")
                task_mod = st.selectbox("Modül", ["Sosyal Medya", "Tasarım", "Yazışma", "Bütçe"])
                task_date = st.date_input("Planlanan Tarih")
                task_prio = st.select_slider("Önem Derecesi", options=["Düşük", "Normal", "Kritik"])
                if st.form_submit_button("Sisteme Kaydet"):
                    st.info(f"'{task_name}' kaydedildi ve takvime işlendi.")
            st.markdown('</div>', unsafe_allow_html=True)

        # 3. Günün Özet Alarmsı
        st.error("🚨 Geciken İşler: 2")

# --- MODÜL DETAYLARI ---
else:
    st.title(main_menu)
    st.info(f"{main_menu} modülü aktif. Bu alandan detaylı raporlama ve dosya takibi yapabilirsiniz.")
    
