# BUILDING A MOVIE RECOMMENDATION SYSTEM

This is a self project done by me Chibuike Victor Akujuobi and reviewed by my friends Teyira Peter Geo-Needam & Emmanuel Ugochukwu. This project was done to enable us strengthen our skills in Python and Machine learning.

## Project Overview
This Movie Recommendation System is a web application that suggests movies based on user input. It combines content-based and collaborative filtering techniques to provide personalized movie recommendations. The system also fetches movie information from the OMDB API and provides links to YouTube trailers for the recommended movies.

## Project Steps
1. **Library Import:** We import the necessary Python libraries, including Flask for building the web app, pandas for data handling, scikit-learn for feature extraction, fuzzywuzzy for fuzzy string matching, requests for API calls, and the Google API Client for YouTube integration.

2. **Data Collection & Preprocessing:** We load and preprocess the movie dataset from a CSV file. The dataset includes information about movies, such as genres, keywords, cast, and directors. Missing values are handled, and a combined feature is created for text-based analysis.

3. **Feature Selection:** We use TF-IDF vectorization to convert the textual features into numerical vectors, which are used for content-based recommendations.

4. **Content-Based Recommendations:** We use fuzzy matching and cosine similarity to find movies similar to the user's input. The content-based recommendations are based on textual features like genres, keywords, and cast.

5. **Collaborative Filtering Recommendations:** Collaborative filtering recommendations are provided if available. These recommendations are based on user ratings and preferences.

6. **Hybrid Recommendations:** We combine both content-based and collaborative filtering recommendations using a weighted approach. Users can adjust the weight of each recommendation type to customize their results.

## Access the Web App
You can access the Movie Recommendation System web app by clicking on the following link:

[Movie Recommendation System](#) _()_

## Feedback Welcome
We value your feedback! If you have any suggestions, encounter issues, or would like to contribute to the project, please feel free to open an issue or pull request on our GitHub repository. Your input is essential in improving this movie recommendation system.

We hope you enjoy using our Movie Recommendation System and discover some great movies to watch!
