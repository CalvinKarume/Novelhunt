import pickle
import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO


st.header('NovelHunt')
model = pickle.load(open('artifacts/model.pkl','rb'))
books_name = pickle.load(open('artifacts/books_name.pkl','rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    books_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        books_name.append(book_pivot.index[book_id])

    for name in books_name[0]:
        ids = np.where(final_rating['Title'] == name)[0][0]
        ids_index.append(ids)

    for ids in ids_index:
        url = final_rating.iloc[ids]['Img_url']
        poster_url.append(url)

    return poster_url


def recommend_book(books_name):
    book_list = []
    book_id= np.where(book_pivot.index == books_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list, poster_url

selected_books = st.selectbox(
    "Type or Select a book",
    books_name
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    image_width = 80

    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1], width=image_width)
    
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2], width=image_width)

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3], width=image_width)

    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4], width=image_width)

    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5], width=image_width)