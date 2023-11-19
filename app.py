import streamlit as st
import pickle 
import numpy as np
import pandas as pd

st.header("Book Recommendation System")
model = pd.read_pickle(open("artifacts/model.pkl","rb"))
Books_Names = pd.read_pickle(open("artifacts/Book_Names.pkl","rb"))
Final_DataFrame_BR = pd.read_pickle(open("artifacts/Final_DataFrame_BR.pkl","rb"))
BookPivot_Table = pd.read_pickle(open("artifacts/BookPivot_Table.pkl","rb"))


def FetchPoster(suggestion):
   BookName = []
   Ids_index = []
   Poster_URL = []

   for book_id in suggestion:
      BookName.append(BookPivot_Table.index[book_id]) # Getting the Books names
    
   for name in BookName[0]:
      # Getting the index of the book
      ids = np.where(Final_DataFrame_BR["Book-Title"] == name)[0][0] 
      Ids_index.append(ids)
    
   for idss in Ids_index:
      url = Final_DataFrame_BR.iloc[idss]["Image-URL-L"]
      Poster_URL.append(url)

   return Poster_URL

def Recommend_Books(Books_Names):
  BooksList = []
  BookId = np.where(BookPivot_Table.index == Books_Names)[0][0]
  distance, suggestion = model.kneighbors(BookPivot_Table.iloc[BookId,:].values.reshape(1,-1),n_neighbors=6)

  Poster_URL = FetchPoster (suggestion)
  for i in range (len(suggestion)):
     Recomm_Books = BookPivot_Table.index[suggestion[i]]
     for j in Recomm_Books:
        BooksList.append(j)
  
  return BooksList, Poster_URL


Books_Selected = st.selectbox(
  "Select the required book", Books_Names)
if st.button("Show Recommendation"):
   Recommendation_Books, Poster_URL = Recommend_Books(Books_Selected)
   col1,col2,col3,col4,col5, col6 = st.columns(6)

   # Getting the recommended book based on the user input
   with col1:
      st.text(Recommendation_Books[1])
      st.image(Poster_URL[1])

   with col2:
      st.text(Recommendation_Books[2])
      st.image(Poster_URL[2])

   with col3:
      st.text(Recommendation_Books[3])
      st.image(Poster_URL[3])

   with col4:
      st.text(Recommendation_Books[4])
      st.image(Poster_URL[4])

   with col5:
      st.text(Recommendation_Books[5])
      st.image(Poster_URL[5])
  
