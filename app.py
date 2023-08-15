import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System Using Machine Learning")
movies = pickle.load(open('artifacts/movie_data.pkl', 'rb'))
similarity_model = pickle.load(open('artifacts/cosine_similarity.pkl', 'rb'))

# function to find the recommended values.
def get_recommendations(movie):
    
    # Get the index of the dataframe that matches the movies
    idx = movies[movies['title'] == movie].index[0]
    #print(idx)
    # Get the pairwsie similarity scores of all data with that movies
    algo_scores = list(enumerate(similarity_model[idx]))
    
    # Sort the data based on the similarity scores
    algo_scores = sorted(algo_scores, key=lambda x: x[1], reverse=True)
    
        
    reco_movie = list()

    # Get the scores of the 5 most similar movies
    for i in algo_scores[1:5]: 
        #print(i)
        #print(movies['title'].iloc[i[0]])
        reco_movie.append(movies['title'].iloc[i[0]])
    
    return reco_movie



movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie for recommendation', 
    movie_list
)

if st.button('Show Recommendation'): 
    recommended_movie = get_recommendations(selected_movie) 

    st.text(recommended_movie[0])
    st.text(recommended_movie[1])
    st.text(recommended_movie[2])
    st.text(recommended_movie[3])
    #st.text(recommended_movie[4])


