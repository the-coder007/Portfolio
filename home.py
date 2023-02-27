import streamlit as st
from PIL import Image
st.title("Innomatics Research Lab Internship Project 1 :ok_hand:")
st.header("Welcome to my Portfolio ! ")
st.subheader(":red[Mritunjay Shawarn]")


col1, col2  = st.columns(2)

col1.markdown(
    """
    #### :blue[Business-Minded Data Scientist with an ability to deliver and demonstrate insights via data analytics and advanced data-driven methods. I identify and integrate data sources and collect structured/unstructured datasets and variables]
    """
)

image = Image.open('mritu.png')
col2.image(image, width=280)

