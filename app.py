import streamlit as st
import requests
from collections import Counter
import re

st.set_page_config(page_title="Evperest Etsy Analyzer", layout="wide")

st.title("EVPEREST ETSY KEYWORD ANALYZER")

st.write("Etsy keyword ve rakip analiz sistemi 🚀")

keyword = st.text_input(
    "Ana Keyword",
    placeholder="Örnek: beige runner"
)

if st.button("ETSY ANALİZ ET"):

    st.info(f"{keyword} için Etsy analiz ediliyor...")

    # ÖRNEK DEMO TITLELAR
    demo_titles = [
        "Beige Kitchen Runner Rug Farmhouse Decor",
        "Neutral Hallway Runner Washable Rug",
        "Farmhouse Kitchen Rug Minimalist Decor",
        "Boho Beige Runner for Kitchen",
        "Modern Neutral Runner Rug"
    ]

    st.subheader("Rakip Titlelar")

    for title in demo_titles:
        st.write("• " + title)

    # Keyword çıkarma
    all_words = []

    for title in demo_titles:
        words = re.findall(r'\\w+', title.lower())
        all_words.extend(words)

    common_words = Counter(all_words).most_common(10)

    st.subheader("En Sık Geçen Keywordler")

    for word, count in common_words:
        st.write(f"{word} → {count} kez")

    st.subheader("Ortalama Fiyat")

    st.success("Tahmini fiyat aralığı: $35 - $70")

    st.subheader("SEO Önerisi")

    st.write("""
    - farmhouse keywordünü kullan
    - neutral decor güçlü görünüyor
    - washable rug yükselen keyword
    - minimalist decor iyi çalışıyor
    """)
