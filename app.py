import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal

# --- SAYFA GENEL AYARLARI ---
st.set_page_config(page_title="TÜRKAK Kurumsal İletişim Portalı", layout="wide")

# --- UI STİLLERİ (Gelişmiş Dashboard & Alarm) ---
st.markdown("""
    <style>
    .main-header { font-size: 28px; font-weight: bold; color: #004a99; margin-bottom: 20px; }
    .alarm-card { background-color: #ff4b4b; color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; text-align: center; font-weight: bold; animation: blinker 2s linear infinite; }
    @keyframes blinker { 50% { opacity: 0.6; } }
    .nav-card { background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #004a99; margin-bottom: 5px; }
    .calendar-cell { height: 120px; border: 1px solid #ddd; padding: 5px; border-radius: 8px; background: white; }
    .task-tag { font-size: 10px; padding: 3px; border-radius: 4px; color: white; margin-bottom: 2px; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# --- SAHTE VERİ HAVUZU (Takvimde Görünmesi İçin) ---
tasks = [
    {"gün": 14, "modül": "Sosyal Medya", "is": "Insta Post", "renk": "#E1306C"},
    {"gün": 14, "modül": "Resmi Yazı", "is": "Gelen Evrak #12", "renk": "#607D8B"},
    {"gün": 15, "modül": "CİMER", "is": "Cevap Bekliyor", "renk": "#D32F2F"},
    {"gün": 18, "modül": "Satın Alma", "is": "Kamera İhalesi", "renk": "#FF9800"},
]

# --- SIDEBAR NAVİGASYON (Her Başlık Bir Sekme) ---
with st.sidebar:
    st.image("https://www.turkak.org.tr/assets/images/logo.png", width=170)
    st.title("SİSTEM MENÜSÜ")
    menu = st.radio("MODÜLLER", [
        "🏠 ANA SAYFA (Takvim)",
        "📱 Sosyal Medya Yönetimi",
        "📄 Resmi Yazışmalar",
        "⚖️ Şikayet / İtiraz",
        "🏛️ CİMER / İleti",
        "🎨 Tasarım Faaliyetleri",
        "📅 Etkinlik Organizasyonu",
        "📧 E-Bülten",
        "💼 Özel Kalem & Bütçe",
        "🛒 Satın Alma Süreçleri"
    ])

# --- 1. ANA SAYFA (FULL SCREEN CALENDAR & SAĞ PANEL) ---
if menu == "🏠 ANA SAYFA (Takvim)":
    col_main, col_side = st.columns([3, 1])

    with col_main:
        st.markdown('<div class="main-header">🗓️ Mayıs 2026 Kurumsal Planlama Takvimi</div>', unsafe_allow_html=True)
        
        # Takvim Mantığı
        yil, ay = 2026, 5
        ay_takvimi = cal.monthcalendar(yil, ay)
        gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        
        t_cols = st.columns(7)
        for i, g in enumerate(gunler): t_cols[i].write(f"**{g}**")

        for hafta in ay_takvimi:
            h_cols = st.columns(7)
            for i, gun in enumerate(hafta):
                if gun != 0:
                    with h_cols[i]:
                        st.markdown(f'<div class="calendar-cell"><b>{gun}</b>', unsafe_allow_html=True)
                        gunluk = [t for t in tasks if t["gün"] == gun]
                        for t in gunluk:
                            st.markdown(f'<div class="task-tag" style="background:{t["renk"]}">{t["is"]}</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="alarm-card">🚨 KRİTİK UYARILAR</div>', unsafe_allow_html=True)
        st.subheader("📌 Günün İşleri")
        st.info("• Sosyal Medya Paylaşımı (14:00)\n• Kurul Toplantısı Hazırlığı")
        
        st.subheader("⏳ Bekleyen Onaylar")
        st.warning("• Afiş Tasarımı (Müdür Onayı)\n• Satın Alma Talebi #12")
        
        st.subheader("🔥 Geciken İşler")
        st.error("• CİMER Yanıtı (-2 Gün)")
        
        st.divider()
        with st.expander("⚡ Hızlı İş Oluştur"):
            st.text_input("Görev Adı")
            st.selectbox("Modül", ["Tasarım", "Yazışma", "Bütçe"])
            st.button("Sisteme Ekle")

# --- 2. SOSYAL MEDYA YÖNETİMİ ---
elif menu == "📱 Sosyal Medya Yönetimi":
    st.title("📱 Sosyal Medya Yönetimi")
    s_tab1, s_tab2, s_tab3 = st.tabs(["Yayın Planı", "İçerik/Tasarım Talebi", "Performans Raporu"])
    with s_tab1:
        st.write("Platformlar: Instagram, X, LinkedIn, YouTube, BlueSky, Next Sosyal")
        st.checkbox("BlueSky paylaşımı yapıldı mı?")

# --- 3. RESMİ YAZIŞMALAR ---
elif menu == "📄 Resmi Yazışmalar":
    st.title("📄 Resmi Yazışma ve Evrak Takibi")
    r_tab1, r_tab2 = st.columns(2)
    with r_tab1:
        st.subheader("Gelen/Giden Evrak")
        st.text_input("Sayı No Giriniz")
    with r_tab2:
        st.subheader("Paraf/Zimmet")
        st.selectbox("Dosya Kimde?", ["Müdür", "Uzman", "Arşiv"])

# --- 4. TASARIM FAALİYETLERİ ---
elif menu == "🎨 Tasarım Faaliyetleri":
    st.title("🎨 Tasarım ve Video Süreç Yönetimi")
    t_tab1, t_tab2, t_tab3 = st.tabs(["Görsel Tasarım", "Video Süreçleri", "Materyal Arşivi"])
    with t_tab2:
        st.info("Video Kurgu -> Montaj -> Revize -> Yayın Teslimi")
        st.slider("Video İlerleme Durumu", 0, 100, 45)

# --- 5. ÖZEL KALEM & BÜTÇE ---
elif menu == "💼 Özel Kalem & Bütçe":
    st.title("💼 Bütçe Yönetimi")
    st.metric("Temsil Ağırlama Giderleri", "₺12.450", "-%2")
    st.write("Etkinlik ve Üst Yönetim harcama takibi")

# --- 6. SATIN ALMA SÜREÇLERİ ---
elif menu == "🛒 Satın Alma Süreçleri":
    st.title("🛒 Satın Alma Yönetimi")
    col1, col2, col3 = st.columns(3)
    col1.button("Teklif Topla")
    col2.button("Fiyat Karşılaştır")
    col3.button("Onay Süreci")
    st.dataframe(pd.DataFrame({"Tedarikçi": ["A Ltd", "B A.Ş"], "Teklif": ["₺50.000", "₺48.500"], "Durum": ["Beklemede", "En Uygun"]}))

# Diğer modüller için benzer yapıları kopyalayabilirsin.
else:
    st.title(menu)
    st.write("Bu modül veri girişi ve akış için hazırdır.")
