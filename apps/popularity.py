import streamlit as st
import pandas as pd
import numpy as np
import pickle
import math
def app():
    st.title("Popular Books")
    @st.cache_data
    def load_data():
        return pickle.load(open('top_rated_books_df.pkl', 'rb'))
    df = load_data()
    books_per_page = 10
    total_pages = math.ceil(len(df) / books_per_page)
    page = st.selectbox("Page", range(1, total_pages + 1))
    start_idx = (page - 1) * books_per_page
    end_idx = start_idx + books_per_page
    books_on_page = df.iloc[start_idx:end_idx]
    for _, book in books_on_page.iterrows():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(book['Image-URL-L'], width=100)
        with col2:
            st.subheader(book['Book-Title'])
            st.write(f"Author: {book['Book-Author']}")
            st.write(f"Average Rating: {book['avg-rating']:.2f}")
            st.write(f"Publisher: {book['Publisher']}")
            st.write(f"Year of Publication: {book['Year-Of-Publication']}")
        st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.write(f"Page {page} of {total_pages}")
    with col3:
        pass
if __name__ == "__main__":
    app()