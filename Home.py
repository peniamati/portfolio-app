import streamlit as st
import pandas
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

profile_image = Image.open("images/profile.jpg")

profile_270 = profile_image.transpose(Image.ROTATE_270)

with col1:
    st.title("Matias Peña")
    st.image(profile_270)

with col2:
    content = """
    Hi, I am Matias! Im Python student programmer, and now im working
    as bird controller in Aeropuerto de Bahia Blanca. Im studying Tecnicatura 
    Universitaria en Programacion at Universidad Provincial del Sudoeste.
    Im looking for a programmer work to start deploying all my knowledge.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built
in Python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

