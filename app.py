import streamlit as st
from collections import Counter
import re

st.set_page_config(page_title="Evperest Etsy SEO Generator", layout="wide")

st.title("EVPEREST ETSY SEO GENERATOR")

st.write("Ücretsiz Etsy SEO title, tag ve description sistemi 🚀")

urun = st.text_input(
    "Ürünü Yaz",
    placeholder="Örnek: beige farmhouse tapestry"
)

if st.button("SEO OLUŞTUR"):

    words = re.findall(r'\w+', urun.lower())

    seo_title = f"{urun.title()} | Farmhouse Decor | Modern Home Style"

    tags = []

    for word in words:
        tags.append(word)
        tags.append(f"{word} decor")

    extra_tags = [
        "etsy decor",
        "modern home",
        "farmhouse style",
        "boho decor",
        "neutral decor",
        "wall decor",
        "minimalist decor",
        "home aesthetic",
        "gift idea",
        "custom decor"
    ]

    tags.extend(extra_tags)

    # tekrar edenleri kaldır
    tags = list(dict.fromkeys(tags))

    # ilk 20 tag
    tags = tags[:20]

    description = f"""
Bring modern style to your home with this beautiful {urun}.

Perfect for:
- Modern interiors
- Farmhouse homes
- Minimalist decoration
- Cozy aesthetic spaces

Features:
- Stylish design
- High quality look
- Trendy Etsy decor style
- Great gift idea

This product is perfect for creating a warm and aesthetic atmosphere.
"""

    pinterest = f"{urun.title()} Decor Inspiration"

    st.subheader("SEO TITLE")
    st.code(seo_title)

    st.subheader("20 ETSY TAG")

    for tag in tags:
        st.write("• " + tag)

    st.subheader("ETSY DESCRIPTION")

    st.text_area(
        "Description",
        description,
        height=250
    )

    st.subheader("PINTEREST TITLE")

    st.code(pinterest)
