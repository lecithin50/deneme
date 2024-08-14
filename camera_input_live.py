import streamlit as st

def camera_input_live():
    picture = st.camera_input("Take a picture")
    if picture:
        return picture
    return None
