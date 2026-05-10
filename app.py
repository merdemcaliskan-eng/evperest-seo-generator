import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Evperest Etsy SEO Generator", layout="wide")

st.title("EVPEREST ETSY SEO GENERATOR")

st.write("AI destekli Etsy SEO title, tag ve description sistemi 🚀")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

urun = st.text_input(
    "Ürünü Yaz",
    placeholder="Örnek: beige farmhouse tapestry"
)

if st.button("SEO OLUŞTUR"):

    with st.spinner("SEO hazırlanıyor..."):

        prompt = f"""
        Sen profesyonel Etsy SEO uzmanısın.

        Ürün:
        {urun}

        Şunları oluştur:

        1. Etsy SEO Title
        - maksimum 140 karakter
        - güçlü keyword kullan
        - Etsy uyumlu olsun

        2. 20 Etsy Tag
        - kısa ve güçlü keywordler
        - Etsy aramalarına uygun olsun

        3. Etsy Description
        - profesyonel
        - satış odaklı
        - modern Etsy diliyle yaz

        4. Pinterest Başlığı

        Düzenli ve okunabilir yaz.
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Sen profesyonel Etsy SEO uzmanısın."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        sonuc = response.choices[0].message.content

        st.subheader("SEO SONUCU")
        st.write(sonuc)
