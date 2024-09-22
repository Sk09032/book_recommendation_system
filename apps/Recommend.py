import streamlit as st
import numpy as np
import pandas as pd
import pickle
@st.cache_data
def load_similarity():
    return pickle.load(open('book_similarity_metrics.pkl', 'rb'))
def load_book_pivot_table():
    return pickle.load(open('books_by_intelli_user_df.pkl', 'rb'))
def load_book_df():
    return pickle.load(open('books_df.pkl', 'rb'))


def get_similar_book(book_name):
    book_index=np.where(load_book_pivot_table().index==book_name)[0][0]
    similar_book=sorted(list(enumerate(load_similarity()[book_index])),key=lambda x:x[1],reverse=True)[1:11]
    recommend_book=[]
    for i in similar_book:
        book_info=[]
        recommend_df=load_book_df()[load_book_df()['Book-Title']==load_book_pivot_table().index[i[0]]]
        book_info.extend(list(recommend_df.drop_duplicates('Book-Title')['Book-Title'].values))
        book_info.extend(list(recommend_df.drop_duplicates('Book-Title')['Book-Author'].values))
        book_info.extend(list(recommend_df.drop_duplicates('Book-Title')['Image-URL-L'].values))
        recommend_book.append(book_info)
    return recommend_book
def app():
    st.title("Get Best book recommendation based on your interest")
    if "submitted_text" not in st.session_state:
        st.session_state.submitted_text = ""
    ls=load_book_pivot_table().index.values
    ls = np.insert(ls, 0, "choose any book from the drop down menu")
    user_input = st.selectbox("Choose your best book",ls)
    if st.button("Submit"):
        if user_input=="choose any book from the drop down menu":
            st.session_state.submitted_text = ""
            st.write("Choose something")
        elif user_input:
            st.session_state.submitted_text = user_input
    if st.session_state.submitted_text:
        st.write("You may also like these books")
        book_list=get_similar_book(st.session_state.submitted_text)
        for book in book_list:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(book[2], width=100)
            with col2:
                st.subheader(book[0])
                st.write(f"Author: {book[1]}")
            st.markdown("---")