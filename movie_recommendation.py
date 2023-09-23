from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import requests
from googleapiclient.discovery import build

app = Flask(__name__)

# OMDB API Configuration
OMDB_API_KEY = 'ca87e68e'  # Replace with your OMDB API key
OMDB_BASE_URL = 'http://www.omdbapi.com/'

# YouTube API Configuration
YOUTUBE_API_KEY = 'AIzaSyAHL96vZ8Lj3tteCdrWzCVdBJsM47hNe6w'  # Replace with your YouTube API key

# Load and preprocess data
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    df[selected_features] = df[selected_features].fillna('')
    df['combined_features'] = df['genres'] + ' ' + df['keywords'] + ' ' + df['tagline'] + ' ' + df['cast'] + ' ' + df['director']
    return df

# Vectorize features
def vectorize_features(df):
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(df['combined_features'])
    return feature_vectors

# Get similar movies using fuzzy matching and cosine similarity
def get_similar_movies(movie_name, df, feature_vectors):
    matches = process.extractOne(movie_name, df['original_title'], scorer=fuzz.partial_ratio)
    if matches[1] < 80:  # Minimum similarity threshold
        return []

    index_of_the_movie = df[df.original_title == matches[0]].index[0]
    similarity = cosine_similarity(feature_vectors[index_of_the_movie:index_of_the_movie + 1], feature_vectors)
    similarity_score = list(enumerate(similarity[0]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    return sorted_similar_movies

# Get movie information from OMDB API
def get_movie_info(movie_title):
    params = {'t': movie_title, 'apikey': OMDB_API_KEY}
    response = requests.get(OMDB_BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Get YouTube trailer URL using the YouTube API
def get_youtube_trailer_url(movie_title, youtube_api_key):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)

    # Search for videos related to the movie title with the keyword "trailer"
    search_response = youtube.search().list(
        q=f"{movie_title} trailer",
        type="video",
        part="id",
        maxResults=1
    ).execute()

    # Extract the video ID of the first search result
    if 'items' in search_response:
        video_id = search_response['items'][0]['id']['videoId']
        youtube_trailer_url = f"https://www.youtube.com/watch?v={video_id}"
        return youtube_trailer_url
    else:
        return None

# Hybrid recommendations
def hybrid_recommendations(movie_name, df, feature_vectors, cf_model=None, cf_weight=0.7):
    # Content-Based Recommendations
    content_based_recommendations = get_similar_movies(movie_name, df, feature_vectors)

    # Collaborative Filtering Recommendations (if available, else empty list)
    cf_recommendations = [] if cf_model is None else cf_model.get_neighbors(movie_name, k=10)

    # Combine Recommendations (Weighted)
    combined_recommendations = []
    for i in range(10):
        content_based_movie = content_based_recommendations[i]
        if cf_recommendations:
            cf_movie = cf_recommendations[i]

            # Weighted combination
            combined_score = (cf_weight * cf_movie.rating) + ((1 - cf_weight) * content_based_movie[1])
            combined_recommendations.append((content_based_movie[0], combined_score))
        else:
            combined_recommendations.append((content_based_movie[0], content_based_movie[1]))

    # Sort combined recommendations by score
    sorted_combined_recommendations = sorted(combined_recommendations, key=lambda x: x[1], reverse=True)

    return sorted_combined_recommendations

# Flask route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_name = request.form['movie_name']
        hybrid_rec = hybrid_recommendations(movie_name, movies, feature_vectors)

        if not hybrid_rec:
            return render_template('index.html', message='Movie not found in the dataset.', movies=movies)
        else:
            recommendations = []

            for movie_id, _ in hybrid_rec[:10]:
                movie_info = get_movie_info(movies.loc[movie_id, 'original_title'])
                if movie_info:
                    youtube_trailer_url = get_youtube_trailer_url(movie_info['Title'], YOUTUBE_API_KEY)
                    if youtube_trailer_url:
                        movie_info['youtube_trailer_url'] = youtube_trailer_url
                    recommendations.append(movie_info)

            return render_template('index.html', recommendations=recommendations, movies=movies)

    return render_template('index.html', message='', movies=movies)

if __name__ == '__main__':
    # Load and preprocess the movie dataset
    dataset_path = "movies.csv"
    movies = load_and_preprocess_data(dataset_path)
    feature_vectors = vectorize_features(movies)

    app.run(debug=True)
