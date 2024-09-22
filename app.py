import streamlit as st
import pandas as pd
from apps import feadback, about, contact,Recommend,popularity

# Setting up the main configuration
st.set_page_config(
    page_title="Get Books",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="auto",
)
# sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About","Collaborative based Recommendation System","Popularity based Recommendation System","Feedback","Contact me"])


# Main app logic
if page == "About":
    about.app()
elif page == "Feedback":
    feadback.app()
elif page == "Contact me":
    contact.app()
elif page == "Collaborative based Recommendation System":
    Recommend.app()
elif page == "Popularity based Recommendation System":
    popularity.app()