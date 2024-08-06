import streamlit as st
import resturant_base

st.title("Resturant Name Generator")
cuisine= st.sidebar.selectbox("Pick a cuisine",("Indian", "Mexican", "Arabic", "Itlian", "French"))

if cuisine:
    response =resturant_base.generate_resturant_name_and_items(cuisine)
    st.header(response['resturant_name'].strip())
    menu_items= response['menu_items'].strip().split(",")
    st.write("--- Menu Items---")

    for item in menu_items:
        st.write(" ",item)