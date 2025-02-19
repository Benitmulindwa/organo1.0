import streamlit as st
from datetime import datetime


def get_molecule_image(name):
    url = f"https://opsin.ch.cam.ac.uk/opsin/{name}.png"

    if url:
        return url
    return None


st.set_page_config(
    page_title="ORGANO",
    page_icon="logo.png",
    layout="centered",
)
st.image("logo.png", width=100)
st.title(
    "ORGANO",
)
st.markdown("**Convert IUPAC name to organic structure**")

iupac_name = st.text_input("Substance name...", "")

if st.button("Submit"):
    if iupac_name:
        with st.spinner("Processing..."):
            image_url = get_molecule_image(iupac_name)
            if image_url:
                st.image(image_url, width=200)
            else:
                st.error("There was an error with the IUPAC name you provided.")
# st.markdown(
#     """<style>body{background-color: #ff06ff}</style>""",
#     unsafe_allow_html=True,
# )
st.markdown(
    f"© {datetime.now().year} built with ❤ by Benit MULINDWA", unsafe_allow_html=True
)
