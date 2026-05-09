import streamlit as st

st.set_page_config(page_title="Evperest Etsy SEO Generator", layout="wide")

st.title("EVPEREST ETSY SEO GENERATOR")
st.write("Runner, masa örtüsü ve duvar örtüsü için hızlı Etsy SEO sistemi")

urun_tipi = st.selectbox(
    "Ürün Tipi",
    ["Runner", "Masa Örtüsü", "Wall Hanging"]
)

renk = st.selectbox(
    "Renk",
    ["Beige", "Black", "Brown", "Cream", "White", "Neutral"]
)

stil = st.selectbox(
    "Stil",
    ["Farmhouse", "Minimalist", "Boho", "Rustic", "Modern"]
)

oda = st.selectbox(
    "Kullanım Alanı",
    ["Kitchen", "Hallway", "Dining Room", "Living Room"]
)

ozellik = st.selectbox(
    "Özellik",
    ["Washable", "Custom", "Neutral Decor", "Soft Texture"]
)

if st.button("SEO OLUŞTUR"):

    title = f"{renk} {oda} {urun_tipi}, {stil} {urun_tipi}, {ozellik} Home Decor"

    tags = [
        f"{oda.lower()} runner",
        f"{stil.lower()} decor",
        f"{renk.lower()} decor",
        f"{ozellik.lower()}",
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

    description = f'''
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
    st.text_area("Description", description, height=250)

    st.subheader("PINTEREST TITLE")
    st.code(pinterest)
