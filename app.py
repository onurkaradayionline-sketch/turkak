import streamlit as st
import pandas as pd
from datetime import datetime
import calendar as cal

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="TÜRKAK İş Takip v1.1", layout="wide")

# --- MODERN UI STİLLERİ ---
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 24px; color: #004a99; }
    .status-card {
        padding: 15px; border-radius: 10px; border: 1px solid #e6e9ef;
        background-color: #ffffff; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    .calendar-day {
        height: 100px; border: 1px solid #f0f2f6; padding: 5px;
        background-color: #fcfcfc; border-radius: 5px;
    }
    .event-tag {
        font-size: 10px; padding: 2px 5px; border-radius: 3px;
        margin-bottom: 2px; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÖRNEK VERİ SETİ (İşlerin Takvimde Görünmesi İçin) ---
events = [
    {"tarih": 14, "is": "Sosyal Medya Paylaşımı", "renk": "#1E90FF"},
    {"tarih": 15, "is": "CİMER Son Gün", "renk": "#FF4B4B"},
    {"tarih": 15, "is": "Bülten Tasarımı", "renk": "#2E8B57"},
    {"tarih": 18, "is": "Toplantı: Satın Alma", "renk": "#FFA500"}
]

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://www.turkak.org.tr/assets/images/logo.png", width=180)
    menu = st.radio("MENÜ", ["📊 Dashboard", "📅 Aylık Planlayıcı", "📁 Modüller", "⚙️ Ayarlar"])

# --- DASHBOARD (Özet Ekranı) ---
if menu == "📊 Dashboard":
    st.title("📌 Operasyonel Özet")
    
    # Üst Metrikler
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Aktif Görevler", "12", "+2")
    m2.metric("Bekleyen Onaylar", "5", "-1")
    m3.metric("Kalan Bütçe", "₺145K", "12%")
    m4.metric("CİMER Performans", "%98", "Hızlı")

    st.divider()
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("🔔 Kritik İş Akışı")
        for ev in events[:3]:
            st.markdown(f"""
                <div class="status-card">
                    <span style="color:{ev['renk']}; font-weight:bold;">● {ev['tarih']} Mayıs:</span> {ev['is']}
                </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.subheader("⚡ Hızlı İşlem")
        st.button("➕ Yeni Görev Tanımla")
        st.button("📑 Rapor Al")
        st.button("📢 Duyuru Yayınla")

# --- AYLIK PLANLAYICI (Takvim Ekranı) ---
elif menu == "📅 Aylık Planlayıcı":
    st.title("🗓️ Mayıs 2026 - İş Takvimi")
    
    # Takvim Mantığı
    yil = 2026
    ay = 5
    ay_takvimi = cal.monthcalendar(yil, ay)
    gunler = ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"]
    
    # Haftanın Günleri Başlığı
    cols = st.columns(7)
    for i, gun in enumerate(gunler):
        cols[i].markdown(f"**{gun}**")
    
    # Takvim Hücreleri
    for hafta in ay_takvimi:
        cols = st.columns(7)
        for i, gun in enumerate(hafta):
            if gun == 0:
                cols[i].write("")
            else:
                with cols[i]:
                    st.markdown(f'<div class="calendar-day"><b>{gun}</b>', unsafe_allow_html=True)
                    # O güne ait işleri filtrele
                    gunluk_isler = [e for e in events if e["tarih"] == gun]
                    for is_oğesi in gunluk_isler:
                        st.markdown(f'<div class="event-tag" style="background-color:{is_oğesi["renk"]}">{is_oğesi["is"]}</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

# --- DİĞER MODÜLLER ---
else:
    st.info("Bu bölüm geliştirme aşamasındadır.")
