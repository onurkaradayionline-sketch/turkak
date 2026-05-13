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

# --- OTURUM YÖNETİMİ & VERİ SAKLAMA ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Görevlerin silinmemesi için session_state üzerinde liste oluşturuyoruz
if "tasks_list" not in st.session_state:
    st.session_state.tasks_list = [
        {"Görev": "CİMER Yanıtı", "Sorumlu": "Davut Kara", "Birim": "CİMER", "Tarih": "2026-05-14"},
        {"Görev": "LinkedIn Post", "Sorumlu": "Onur Karadayı", "Birim": "Sosyal Medya", "Tarih": "2026-05-15"}
    ]

# Personel Listesi
personel_listesi = ["Onur Karadayı", "Uğur Onur", "Umut Halaza", "Davut Kara"]

# --- MODERN TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .ticker-wrap {
        width: 100%; overflow: hidden; background: #ffffff; 
        color: #e30613; padding: 10px 0; border-radius: 8px; 
        margin-bottom: 15px; border: 1px solid #e0e0e0; font-size: 14px;
    }
    .ticker { display: inline-block; white-space: nowrap; animation: ticker 40s linear infinite; }
    @keyframes ticker { 0% { transform: translate3d(0, 0, 0); } 100% { transform: translate3d(-100%, 0, 0); } }
    .header-container {
        display: flex; align-items: center; background: #ffffff; 
        padding: 15px; border-radius: 12px; border-top: 5px solid #e30613;
        margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .system-title { font-size: clamp(16px, 4vw, 22px); font-weight: 800; color: #333; margin-left: 15px; }
    .action-card {
        background: #ffffff; padding: 20px; border-radius: 12px;
        border: 1px solid #e0e0e0; margin-bottom: 15px; 
    }
    .action-card h3 { color: #e30613; font-size: 18px; margin-bottom: 12px; }
    .cal-scroll-container { overflow-x: auto; background: white; padding: 15px; border-radius: 12px; border: 1px solid #ddd; }
    .cal-table { width: 100%; min-width: 600px; border-collapse: collapse; }
    .cal-table th { background: #f8f9fa; padding: 10px; border: 1px solid #eee; text-align: center; }
    .cal-table td { width: 14.28%; height: 85px; border: 1px solid #eee; vertical-align: top; padding: 5px; }
    .cal-day-num { color: #e30613; font-weight: bold; }
    .cal-task-tag { font-size: 9px; background: #ffebee; color: #e30613; padding: 2px; border-radius: 3px; margin-top: 2px; display: block; overflow: hidden; }
    div.stButton > button { width: 100% !important; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST HABER BANDI ---
st.markdown('<div class="ticker-wrap"><div class="ticker">🚨 KRİTİK: CİMER Yanıt Süresi (2 Gün) | 📢 YENİ: Haftalık Bülten Yayına Hazır | ⚖️ BİLGİ: Şikayet Dosyası #882 İnceleniyor</div></div>', unsafe_allow_html=True)

# --- ÜST PANEL ---
st.markdown(f"""
    <div class="header-container">
        <img src="https://upload.wikimedia.org/wikipedia/tr/b/b2/T%C3%BCrk_Akreditasyon_Kurumu_logosu.png" width="60">
        <div class="system-title">TÜRKAK Kurumsal İletişim Portalı</div>
    </div>
    """, unsafe_allow_html=True)

# --- SOL MENÜ ---
with st.sidebar:
    st.markdown("### 🏢 KURUMSAL MODÜLLER")
    menu = st.radio("", [
        "🏠 Dashboard & Takvim", "📱 Sosyal Medya", "📄 Resmi Yazışmalar", 
        "⚖️ Şikayet / İtiraz", "🏛️ CİMER / İleti", "🎨 Tasarım Faaliyetleri", 
        "📅 Etkinlik / Organizasyon", "📧 E-Bülten İşlemleri", "💼 Özel Kalem & Bütçe", "🛒 Satın Alma / İhale"
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
    # Dijital Göstergeler (Dinamik)
    cols = st.columns(4)
    titles = ["Bekleyen", "Acil", "Personel", "CİMER"]
    vals = [str(len(st.session_state.tasks_list)), "02", "4", "4.9"]
    for i, col in enumerate(cols):
        col.markdown(f'<div style="background:white; padding:15px; border-radius:10px; border-bottom:3px solid #e30613; text-align:center;"><div style="font-size:12px; color:#666;">{titles[i]}</div><div style="font-size:24px; font-weight:bold; color:#e30613;">{vals[i]}</div></div>', unsafe_allow_html=True)

    st.write("")
    col_main, col_right = st.columns([2.2, 1])

    with col_main:
        st.subheader("🗓️ Kurumsal Takvim (Mayıs 2026)")
        cal_html = '<div class="cal-scroll-container"><table class="cal-table"><thead><tr>'
        for d in ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]: cal_html += f'<th>{d}</th>'
        cal_html += '</tr></thead><tbody>'
        
        month_days = cal.monthcalendar(2026, 5)
        for week in month_days:
            cal_html += '<tr>'
            for day in week:
                if day == 0: cal_html += '<td></td>'
                else:
                    tasks_today = [t for t in st.session_state.tasks_list if datetime.strptime(t['Tarih'], '%Y-%m-%d').day == day]
                    task_markup = ""
                    for t in tasks_today:
                        task_markup += f'<span class="cal-task-tag">{t["Sorumlu"][:10]}..: {t["Görev"][:10]}</span>'
                    cal_html += f'<td><span class="cal-day-num">{day}</span>{task_markup}</td>'
            cal_html += '</tr>'
        cal_html += '</tbody></table></div>'
        st.markdown(cal_html, unsafe_allow_html=True)

    with col_right:
        # Ekip Girişi
        st.markdown('<div class="action-card"><h3>👤 Ekip Girişi</h3>', unsafe_allow_html=True)
        if not st.session_state.logged_in:
            u = st.text_input("Kullanıcı Adı")
            p = st.text_input("Şifre", type="password")
            if st.button("Giriş Yap"):
                if u == "turkak" and p == "1234":
                    st.session_state.logged_in = True
                    st.session_state.user_name = u
                    st.rerun()
                else: st.error("Hatalı Giriş!")
        else: st.info(f"Hoş geldin, **{st.session_state.user_name}**")
        st.markdown('</div>', unsafe_allow_html=True)

        # Yeni Görev Girişi (AKTİF)
        st.markdown('<div class="action-card"><h3>➕ Yeni Görev Tanımla</h3>', unsafe_allow_html=True)
        if st.session_state.logged_in:
            with st.form("task_form", clear_on_submit=True):
                new_task_name = st.text_input("Görev Başlığı")
                new_task_person = st.selectbox("Sorumlu Personel", personel_listesi)
                new_task_cat = st.selectbox("Modül", ["Sosyal Medya", "CİMER", "Tasarım", "Yazışma"])
                new_task_date = st.date_input("Teslim Tarihi", value=datetime(2026, 5, 14))
                
                if st.form_submit_button("Sisteme İşle ve Ata"):
                    if new_task_name:
                        st.session_state.tasks_list.append({
                            "Görev": new_task_name,
                            "Sorumlu": new_task_person,
                            "Birim": new_task_cat,
                            "Tarih": str(new_task_date)
                        })
                        st.success(f"Görev {new_task_person} kişisine atandı!")
                        st.rerun()
                    else:
                        st.warning("Lütfen görev başlığı girin.")
        else: st.warning("Görev atamak için giriş yapın.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DİĞER MODÜLLER ---
else:
    st.title(f"📂 {menu}")
    st.subheader(f"{menu} Personel İş Yükü")
    # Filtrelenmiş görevleri göster
    current_tasks = [t for t in st.session_state.tasks_list if t['Birim'] in menu or menu.startswith(t['Birim'])]
    if current_tasks:
        st.table(pd.DataFrame(current_tasks))
    else:
        st.info("Bu modül için atanmış aktif görev bulunmuyor.")
