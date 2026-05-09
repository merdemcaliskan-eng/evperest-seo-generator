import streamlit as st
import pandas as pd
from openai import OpenAI

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

ana_keyword = st.text_input(
    "Ana Keyword",
    placeholder="Örnek: beige runner"
)

st.info("AI destekli Etsy SEO sistemi aktif 🚀")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

free_text = st.text_input(
    "Ürünü Yaz",
    placeholder="Örnek: beige farmhouse tapestry"
)

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

    ai_prompt = f"""
    Sen profesyonel Etsy SEO uzmanısın.

    Kullanıcının ürünü:
    {free_text}

    Şunları üret:
    1. SEO title
    2. 13 Etsy tag
    3. Etsy açıklaması
    4. Pinterest başlığı

    Modern Etsy SEO mantığına uygun yaz.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Sen profesyonel Etsy SEO uzmanısın."},
            {"role": "user", "content": ai_prompt}
        ]
    )

    ai_result = response.choices[0].message.content

    st.subheader("AI SEO SONUCU")
    st.write(ai_result)

    seo_skoru = 85

    seo_skoru = 85

    onerilen_kelime = [
        "neutral decor",
        "farmhouse decor",
        "minimalist rug",
        "washable runner",
        "boho decor"
    ]

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

    st.subheader("SEO SKORU")
    st.progress(seo_skoru)
    st.write(f"SEO Skoru: {seo_skoru}/100")

    st.subheader("ÖNERİLEN KEYWORDS")
    for kelime in onerilen_kelime:
        st.write(f"✓ {kelime}")

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
