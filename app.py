import pandas as pd
import streamlit as st
movies=pd.read_csv('movies.csv')
def recommend(num):
  movies=movies.groupby('title')[['popularity','weighted_votes']].mean().reset_index()
  movies=movies.sort_values(['weighted_votes','popularity'],ascending=False)[:n]
  return list(movies['title'])
st.title('Popularity Based Recommendation System')
num=st.number_input('Choose the number of movies to recommend')
list_of_movies=recommend(num)
if st.button('Show Movies'):
  st.header(f'Top {num} Movies are :')
  for movie in list_of_movies:
    st.subheader(movie)