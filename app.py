import streamlit as st
import pandas as pd

st.set_page_config(page_title="Evperest Etsy SEO Generator", layout="wide")

st.title("EVPEREST ETSY SEO GENERATOR V1")

with st.sidebar:
    st.header("Yönetim Paneli")

    urunler_text = st.text_area(
        "Ürün Tipleri",
        "Runner,Masa Örtüsü,Wall Hanging"
    )

    renkler_text = st.text_area(
        "Renkler",
        "Beige,Black,Brown,Cream,White,Neutral"
    )

    stiller_text = st.text_area(
        "Stiller",
        "Farmhouse,Minimalist,Boho,Rustic,Modern"
    )

    alanlar_text = st.text_area(
        "Kullanım Alanları",
        "Kitchen,Hallway,Dining Room,Living Room"
    )

    ozellikler_text = st.text_area(
        "Özellikler",
        "Washable,Custom,Neutral Decor,Soft Texture"
    )

urunler = [x.strip() for x in urunler_text.split(",")]
renkler = [x.strip() for x in renkler_text.split(",")]
stiller = [x.strip() for x in stiller_text.split(",")]
alanlar = [x.strip() for x in alanlar_text.split(",")]
ozellikler = [x.strip() for x in ozellikler_text.split(",")]
st.write("Runner, masa örtüsü ve duvar örtüsü için hızlı Etsy SEO sistemi")

# Ürün Bilgileri
urun_tipi = st.selectbox(
    "Ürün Tipi",
    urunler
)

renk = st.selectbox(
    "Renk",
    renkler
)

stil = st.selectbox(
    "Stil",
    stiller
)

oda = st.selectbox(
    "Kullanım Alanı",
    alanlar
)

özellik = st.selectbox(
    "Özellik",
    ozellikler
)

# SEO Üretici
if st.button("SEO OLUŞTUR"):

    title = f"{renk} {oda} {urun_tipi}, {stil} {urun_tipi}, {özellik} Home Decor"

    tags = [
        f"{oda.lower()} runner",
        f"{stil.lower()} decor",
        f"{renk.lower()} decor",
        f"{özellik.lower()}",
        "minimalist home",
        "neutral decor",
        "modern farmhouse",
        "boho decor",
        "washable rug",
        "custom decor",
        "hallway runner",
        "kitchen decor",
        "home styling"
    ]

    açıklama = f'''
Transform your home with this {stil.lower()} and elegant {urun_tipi.lower()}.

Features:
- Premium quality
- Personalized production
- Modern minimalist style
- Easy to clean
- Neutral decor compatible

Perfect for:
- Modern homes
- Farmhouse interiors
- Kitchen styling
- Hallway decoration

Each product is specially produced for your order.
'''

    pinterest = f"{renk} {stil} {urun_tipi} Decor"

    st.subheader("SEO TITLE")
    st.code(title)

    st.subheader("13 TAG")
    for tag in tags:
        st.write(f"- {tag}")

    st.subheader("AÇIKLAMA")
    st.text_area("Description", açıklama, height=250)

    st.subheader("PINTEREST TITLE")
    st.code(pinterest)

st.divider()

st.subheader("GELECEK SÜRÜMLER")

st.write("""
- Etsy trend analizi
- Rakip title analizi
- Otomatik keyword sistemi
- Etsy scraping
- Trend ürün bulucu
- Pinterest pin generator
- Çoklu listing üretici
- Gerçek Etsy SEO skoru
""")
