import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

popular_book_df=pd.read_csv('top_rated_books_df.csv')


st.title('Hello')
st.dataframe(popular_book_df)