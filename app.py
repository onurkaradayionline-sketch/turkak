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

# --- OTURUM YÖNETİMİ ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# --- GELİŞMİŞ MOBİL & KURUMSAL TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #1e1e1e; }
    
    /* Haber Bandı */
    .ticker-wrap {
        width: 100%; overflow: hidden; background: #ffffff; 
        color: #e30613; padding: 10px 0; border-radius: 8px; 
        margin-bottom: 15px; border: 1px solid #e0e0e0; font-size: 14px;
    }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 40s linear infinite; }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }

    /* Header */
    .header-container {
        display: flex; align-items: center; background: #ffffff; 
        padding: 15px; border-radius: 12px; border-top: 5px solid #e30613;
        margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .system-title { font-size: clamp(16px, 4vw, 22px); font-weight: 800; color: #333; margin-left: 15px; }

    /* Kartlar */
    .action-card {
        background: #ffffff; padding: 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; margin-bottom: 15px; 
    }
    .action-card h3 { color: #e30613; font-size: 18px; margin-bottom: 12px; }

    /* TAKVİM - MOBİLDE KAYDIRILABİLİR KUTU YAPISI */
    .cal-scroll-container {
        overflow-x: auto;
        background: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #ddd;
    }
    .cal-table {
        width: 100%;
        min-width: 600px; /* Mobilde dikey yerine yatay kaydırmayı zorunlu kılar */
        border-collapse: collapse;
    }
    .cal-table th { background: #f8f9fa; padding: 10px; border: 1px solid #eee; text-align: center; }
    .cal-table td { width: 14.28%; height: 80px; border: 1px solid #eee; vertical-align: top; padding: 5px; }
    .cal-day-num { color: #e30613; font-weight: bold; }
    .cal-task-tag { font-size: 9px; background: #ffebee; color: #e30613; padding: 2px; border-radius: 3px; margin-top: 2px; display: block; }

    /* Buton Genişlikleri */
    div.stButton > button { width: 100% !important; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST HABER BANDI ---
st.markdown('<div class="ticker-wrap"><div class="ticker">🚨 KRİTİK: CİMER Yanıt Süresi (2 Gün) | 📢 YENİ: Haftalık Bülten Yayına Hazır | ⚖️ BİLGİ: Şikayet Dosyası #882 İnceleniyor | 🛒 SATIN ALMA: Kırtasiye İhalesi Onayda</div></div>', unsafe_allow_html=True)

# --- ÜST PANEL ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/tr/b/b2/T%C3%BCrk_Akreditasyon_Kurumu_logosu.png" width="60">
        <div class="system-title">TÜRKAK Kurumsal İletişim Portalı</div>
    </div>
    """, unsafe_allow_html=True)

# --- TÜM ANA BAŞLIKLARI İÇEREN AKTİF SOL MENÜ ---
with st.sidebar:
    st.markdown("### 🏢 KURUMSAL MODÜLLER")
    menu = st.radio("", [
        "🏠 Dashboard & Takvim",
        "📱 Sosyal Medya",
        "📄 Resmi Yazışmalar",
        "⚖️ Şikayet / İtiraz",
        "🏛️ CİMER / İleti",
        "🎨 Tasarım Faaliyetleri",
        "📅 Etkinlik / Organizasyon",
        "📧 E-Bülten İşlemleri",
        "💼 Özel Kalem & Bütçe",
        "🛒 Satın Alma / İhale"
    ])
    st.divider()
    if st.session_state.logged_in:
        st.success(f"Oturum: {st.session_state.user_name}")
        if st.button("Çıkış Yap"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.warning("Giriş Yapılmadı")

# --- DASHBOARD & TAKVİM ---
if menu == "🏠 Dashboard & Takvim":
    # Dijital Göstergeler
    cols = st.columns(4)
    titles = ["Bekleyen", "Acil", "Bütçe", "CİMER"]
    vals = ["14", "02", "%62", "4.9"]
    for i, col in enumerate(cols):
        col.markdown(f'<div style="background:white; padding:15px; border-radius:10px; border-bottom:3px solid #e30613; text-align:center;"><div style="font-size:12px; color:#666;">{titles[i]}</div><div style="font-size:24px; font-weight:bold; color:#e30613;">{vals[i]}</div></div>', unsafe_allow_html=True)

    st.write("")
    col_main, col_right = st.columns([2.2, 1])

    with col_main:
        st.subheader("🗓️ Kurumsal Takvim (Mayıs 2026)")
        # Mobilde kutu gibi görünen yatay kaydırılabilir takvim
        cal_html = '<div class="cal-scroll-container"><table class="cal-table"><thead><tr>'
        for d in ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]: cal_html += f'<th>{d}</th>'
        cal_html += '</tr></thead><tbody>'
        
        month_days = cal.monthcalendar(2026, 5)
        for week in month_days:
            cal_html += '<tr>'
            for day in week:
                if day == 0: cal_html += '<td></td>'
                else:
                    task = ""
                    if day == 14: task = '<span class="cal-task-tag">CİMER Son</span>'
                    if day == 20: task = '<span class="cal-task-tag">Bülten Yayını</span>'
                    cal_html += f'<td><span class="cal-day-num">{day}</span>{task}</td>'
            cal_html += '</tr>'
        cal_html += '</tbody></table></div>'
        st.markdown(cal_html, unsafe_allow_html=True)

    with col_right:
        # Üye Girişi
        st.markdown('<div class="action-card"><h3>👤 Ekip Girişi</h3>', unsafe_allow_html=True)
        if not st.session_state.logged_in:
            u = st.text_input("Kullanıcı Adı")
            p = st.text_input("Şifre", type="password")
            if st.button("Giriş Yap"):
                if u == "turkak" and p == "1234":
                    st.session_state.logged_in = True
                    st.session_state.user_name = u
                    st.rerun()
                else: st.error("Hata!")
        else: st.info(f"Hoş geldin, **{st.session_state.user_name}**")
        st.markdown('</div>', unsafe_allow_html=True)

        # Yeni İş
        st.markdown('<div class="action-card"><h3>➕ Yeni Görev</h3>', unsafe_allow_html=True)
        if st.session_state.logged_in:
            st.text_input("Görev Adı")
            st.selectbox("Modül", ["Sosyal Medya", "CİMER", "Tasarım"])
            st.button("Kaydet")
        else: st.warning("Giriş yapın.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DİĞER MODÜLLER (Örnek İşlerle) ---
else:
    st.title(f"📂 {menu}")
    
    # Her başlık için farklı örnek veri gösterimi
    data = {
        "📱 Sosyal Medya": ["Haftalık LinkedIn Paylaşım Planı", "Akreditasyon Haftası Video Prodüksiyonu", "Twitter (X) Etkileşim Raporu"],
        "📄 Resmi Yazışmalar": ["Dışişleri Bakanlığı Gelen Evrak Yanıtı", "Kurum İçi Görevlendirme Yazısı", "Arşiv Dijitalleştirme Çalışması"],
        "⚖️ Şikayet / İtiraz": ["Dosya #2026/04: Laboratuvar İtirazı", "Müşteri Memnuniyeti Anketi Analizi"],
        "🏛️ CİMER / İleti": ["Vatandaş Başvurusu #4412 (Acil)", "CİMER Aylık İstatistik Raporu"],
        "🎨 Tasarım Faaliyetleri": ["Sertifika Şablonu Güncellemesi", "E-Bülten Banner Tasarımları", "Kurumsal Kimlik Kılavuzu Revizyonu"],
        "📅 Etkinlik / Organizasyon": ["14 Mayıs Akreditasyon Günü Resepsiyonu", "Bölgesel Eğitim Semineri - Ankara"],
        "📧 E-Bülten İşlemleri": ["Sayı 42: Teknik Makaleler Derlemesi", "Abone Listesi Temizliği"],
        "💼 Özel Kalem & Bütçe": ["Müdürlük Aylık Harcama Raporu", "Temsil ve Tören Giderleri Takibi"],
        "🛒 Satın Alma / İhale": ["Yıllık Sunucu Lisans Alımı", "Kırtasiye Malzemesi Teklif Toplama"]
    }
    
    st.subheader("📌 Aktif İş Listesi")
    for task in data.get(menu, ["Genel İş Takibi"]):
        st.info(f"✅ {task}")
    
    if st.session_state.logged_in:
        st.button(f"{menu} İçin Dosya Yükle")
