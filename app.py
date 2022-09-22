import streamlit as st

st.title("Hello Let's find whether an URL is DGA or Not!")

if st.button('Check DGA'):
    dga_url=st.text_input("Enter the URL")
    st.title(dga_url)
    clean = 0.262
    DGA = 0.92
    st.number_input('clean', clean)
    st.number_input('DGA', DGA)