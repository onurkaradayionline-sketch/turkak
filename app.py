import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="TÜRKAK İş Yönetim Sistemi",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- OTURUM YÖNETİMİ (Giriş Mekanizması) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# --- MODERN VE AYDINLIK TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; color: #1e1e1e; }
    .ticker-wrap {
        width: 100%; overflow: hidden; background: #ffffff; 
        color: #e30613; padding: 12px 0; border-radius: 10px; 
        margin-bottom: 20px; border: 1px solid #e0e0e0; font-weight: 600;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .ticker { display: inline-block; white-space: nowrap; padding-right: 100%; animation: ticker 40s linear infinite; }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
    .header-container {
        display: flex; align-items: center; background: #ffffff; 
        padding: 20px 30px; border-radius: 15px; border-top: 5px solid #e30613;
        margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .system-title { font-size: 26px; font-weight: 800; color: #333; margin-left: 20px; }
    .action-card {
        background: #ffffff; padding: 25px; border-radius: 15px;
        border: 1px solid #e0e0e0; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    .action-card h3 { color: #e30613; font-size: 20px; margin-bottom: 15px; border-bottom: 2px solid #f0f2f5; padding-bottom: 10px; }
    .stat-card {
        background: #ffffff; padding: 20px; border-radius: 12px;
        text-align: center; border-bottom: 4px solid #e30613; box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    .stat-val { font-size: 30px; font-weight: 800; color: #e30613; }
    .stat-label { color: #666; font-size: 14px; font-weight: 600; }
    .cal-day { min-height: 110px; background: #ffffff; border-radius: 10px; padding: 10px; border: 1px solid #eee; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST KAYAR YAZI ---
st.markdown("""
    <div class="ticker-wrap">
        <div class="ticker">
            📢 GÜNCEL: Yeni Satın Alma Modülü Aktif Edildi | 🚨 ACİL: CİMER Yanıt Süresine Son 48 Saat | 📱 SOSYAL MEDYA: Haftalık Planlama Onay Bekliyor | ✅ TAMAMLANDI: E-Bülten Tasarımı Arşive Gönderildi
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- ÜST PANEL ---
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/tr/b/b2/T%C3%BCrk_Akreditasyon_Kurumu_logosu.png", width=110)
with col_title:
    st.markdown('<div class="system-title">Kurumsal İletişim Müdürlüğü İş Yönetim Sistemi</div>', unsafe_allow_html=True)

# --- AKTİF SOL SIDEBAR ---
with st.sidebar:
    st.markdown("### 📋 ANA MODÜLLER")
    menu = st.radio("", [
        "🏠 Dashboard & Takvim", "📱 Sosyal Medya Yönetimi", "📄 Resmi Yazışmalar", 
        "⚖️ Şikayet / İtiraz", "🏛️ CİMER / İleti", "🎨 Tasarım Faaliyetleri", 
        "📅 Etkinlik Organizasyonu", "📧 E-Bülten", "💼 Özel Kalem & Bütçe", "🛒 Satın Alma Süreçleri"
    ])
    st.divider()
    if st.session_state.logged_in:
        st.success(f"Oturum Açık: {st.session_state.user_name}")
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.warning("Lütfen giriş yapın.")
    st.divider()
    st.caption(f"TÜRKAK v3.1 | {datetime.now().strftime('%d.%m.%Y')}")

# --- İÇERİK AKIŞI ---
if menu == "🏠 Dashboard & Takvim":
    g1, g2, g3, g4 = st.columns(4)
    g1.markdown('<div class="stat-card"><div class="stat-label">Bekleyen İş</div><div class="stat-val">12</div></div>', unsafe_allow_html=True)
    g2.markdown('<div class="stat-card"><div class="stat-label">Acil Görev</div><div class="stat-val">04</div></div>', unsafe_allow_html=True)
    g3.markdown('<div class="stat-card"><div class="stat-label">Bütçe Kullanımı</div><div class="stat-val">%62</div></div>', unsafe_allow_html=True)
    g4.markdown('<div class="stat-card"><div class="stat-label">CİMER Puanı</div><div class="stat-val">4.8</div></div>', unsafe_allow_html=True)

    st.write("")
    col_main, col_right = st.columns([2, 1])

    with col_main:
        st.subheader("🗓️ Aylık İş Planı")
        cal_data = cal.monthcalendar(2026, 5)
        d_cols = st.columns(7)
        for i, d in enumerate(["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]): d_cols[i].caption(f"**{d}**")
        for week in cal_data:
            w_cols = st.columns(7)
            for i, day in enumerate(week):
                if day != 0:
                    with w_cols[i]:
                        st.markdown(f'<div class="cal-day"><b style="color:#e30613;">{day}</b></div>', unsafe_allow_html=True)

    with col_right:
        # --- AKTİF GİRİŞ PANELİ ---
        st.markdown('<div class="action-card"><h3>👤 Ekip Üyesi Girişi</h3>', unsafe_allow_html=True)
        if not st.session_state.logged_in:
            user_input = st.text_input("Kullanıcı Adı")
            pass_input = st.text_input("Şifre", type="password")
            if st.button("Giriş Yap", use_container_width=True):
                if user_input == "turkak" and pass_input == "1234": # Burayı değiştirebilirsin
                    st.session_state.logged_in = True
                    st.session_state.user_name = user_input
                    st.success("Başarıyla giriş yapıldı!")
                    st.rerun()
                else:
                    st.error("Hatalı kullanıcı adı veya şifre!")
        else:
            st.info(f"Hoş geldin, **{st.session_state.user_name}**. Sisteme yetkili giriş yapıldı.")
        st.markdown('</div>', unsafe_allow_html=True)

        # --- AKTİF İŞ GİRİŞ PANELİ ---
        st.markdown('<div class="action-card"><h3>➕ Yeni İş Tanımla</h3>', unsafe_allow_html=True)
        if st.session_state.logged_in:
            task_title = st.text_input("İş Başlığı")
            task_cat = st.selectbox("İlgili Birim", ["Sosyal Medya", "CİMER", "Tasarım", "Satın Alma"])
            task_date = st.date_input("Teslim Tarihi")
            if st.button("Sisteme İşle", use_container_width=True):
                st.success(f"'{task_title}' görevi başarıyla kaydedildi!")
        else:
            st.warning("Yeni iş eklemek için lütfen giriş yapın.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.title(menu)
    st.info(f"{menu} modülüne hoş geldiniz.")
