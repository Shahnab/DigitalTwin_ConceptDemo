import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

col1, mid, col2= st.columns([1,1,20])
with col1:
    st.image("logo.jpg", width=150)
with col2:
    st.markdown("# Digital Consumer Twin")
    st.markdown( " Research Playground Concept Demo--- Female Shopper in Skincare Category")
    st.markdown("Serve as a valuable reference source for brand managers and agency partners- Can ask questions related to skincare products to create integrated marketing strategies and media initiatives")


# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://ora.ai/embed/f8b42ab4-e0d3-4223-905c-37a01334475e", width=1450, height=600, scrolling=True)

