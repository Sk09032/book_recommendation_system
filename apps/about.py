import streamlit as st

def app():
    st.title("Welcome to the Book Recommendation System")
    st.write("""
    Welcome to our Book Recommendation System! This application is designed to help book lovers discover 
    new reads based on their preferences and reading history.
    """)
    
    st.header("How it works")
    st.write("""
    1. I analyze thousands of books and user ratings.
    2. This recommendation system uses two type of functionality First one is Popularity based Second is collaborative based using users rating.
    """)
    
    st.header("Our Team")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Sunny Kumar")
        st.write("Data Scientist")
        st.markdown("[Check out my GitHub](https://github.com/Sk09032)")
    
    st.header("Version Information")
    st.write("Current Version: 1.0.0")
    st.write("Last Updated: September 21, 2024")

if __name__ == "__main__":
    app()