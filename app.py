import pandas as pd
import streamlit as st
movies=pd.read_csv('movies.csv')
def recommend(movies,num):
  movies=movies.groupby('title')[['popularity','weighted_votes']].mean().reset_index()
  movies=movies.sort_values(['weighted_votes','popularity'],ascending=False)
  return list(movies['title'])[:num]
st.title('Popularity Based Recommendation System')
num=st.number_input('Choose the number of movies to recommend',1,value=10,step=1)
list_of_movies=recommend(movies,num)
if st.button('Show Movies'):
  st.header(f'Top {num} Movies are :')
  for movie in list_of_movies:
    st.subheader(movie)