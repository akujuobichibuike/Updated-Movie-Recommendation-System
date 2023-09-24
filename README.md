# Movie Recommendation System

This Movie Recommendation System is a web application that suggests movies based on user input. It combines content-based and collaborative filtering techniques to provide personalized movie recommendations. The system also fetches movie information from the OMDB API and provides links to YouTube trailers for the recommended movies.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Steps](#project-steps)
3. [Getting Started](#getting-started)
4. [Access the Web App](#access-the-web-app)
5. [Feedback Welcome](#feedback-welcome)
6. [Future Enhancements](#future-enhancements)
7. [Testing](#testing)

## Project Overview
This project, undertaken by Chibuike Victor Akujuobi, Teyira Peter Geo-Needam, and Emmanuel Ugochukwu, was designed to strengthen our skills in Python and Machine Learning. The Movie Recommendation System provides movie suggestions based on a user's preferences, using a combination of content-based and collaborative filtering techniques.

### Project Steps
1. **Library Import:** We import the necessary Python libraries, including Flask for building the web app, pandas for data handling, scikit-learn for feature extraction, fuzzywuzzy for fuzzy string matching, requests for API calls, and the Google API Client for YouTube integration.

2. **Data Collection & Preprocessing:** We load and preprocess the movie dataset from a CSV file. The dataset includes information about movies, such as genres, keywords, cast, and directors. Missing values are handled, and a combined feature is created for text-based analysis.

3. **Feature Selection:** We use TF-IDF vectorization to convert the textual features into numerical vectors, which are used for content-based recommendations.

4. **Content-Based Recommendations:** Fuzzy matching and cosine similarity are employed to find movies similar to the user's input. Content-based recommendations are based on textual features like genres, keywords, and cast.

5. **Collaborative Filtering Recommendations:** Collaborative filtering recommendations are provided if available. These recommendations are based on user ratings and preferences.

6. **Hybrid Recommendations:** We combine both content-based and collaborative filtering recommendations using a weighted approach. Users can adjust the weight of each recommendation type to customize their results.

### Getting Started
To run this project locally, follow these steps:
1. Clone the repository.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Run the web application by executing `python app.py` in your terminal.

### Access the Web App
You can access the Movie Recommendation System web app by clicking on the following link:
[Movie Recommendation System](https://chibuikeakujuobi-recommendation.onrender.com)

### Feedback Welcome
We value your feedback! If you have any suggestions, encounter issues, or would like to contribute to the project, please feel free to open an issue or pull request on our [GitHub repository](https://github.com/your-username/repo-name). Your input is essential in improving this movie recommendation system.

### Future Enhancements
We plan to continue enhancing the Movie Recommendation System in the following ways:
- Implement user authentication to provide more personalized recommendations.
- Explore advanced collaborative filtering techniques such as matrix factorization.
- Enhance the user interface for a more seamless experience.
- Collect and analyze user feedback to improve recommendation quality.

### Testing
We have rigorously tested the recommendation system to ensure its accuracy and performance. Metrics such as precision, recall, and user satisfaction have been considered during testing.

We hope you enjoy using our Movie Recommendation System and discover some great movies to watch!
