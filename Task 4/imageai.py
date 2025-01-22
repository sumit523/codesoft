import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

data = {
    "movie_id": [1, 2, 3, 4, 5],
    "title": ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"],
    "genre": ["Sci-Fi Action", "Sci-Fi Thriller", "Sci-Fi Drama", "Action Crime", "Crime Drama"]
}
movies = pd.DataFrame(data)

user_data = {
    "user_id": [1, 1, 2, 2, 3, 3, 4],
    "movie_id": [1, 2, 2, 3, 4, 5, 1],
    "rating": [5, 4, 4, 5, 5, 3, 4]
}
ratings = pd.DataFrame(user_data)

user_item_matrix = ratings.pivot_table(index="user_id", columns="movie_id", values="rating").fillna(0)
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_movies_cf(user_id, user_item_matrix, user_similarity_df, movies, top_n=3):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    user_ratings = user_item_matrix.loc[user_id]
    recommendations = {}
    for similar_user in similar_users:
        for movie_id, rating in user_item_matrix.loc[similar_user].items():
            if movie_id not in user_ratings or user_ratings[movie_id] == 0:
                recommendations[movie_id] = recommendations.get(movie_id, 0) + rating
    recommended_movies = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return movies[movies['movie_id'].isin([movie[0] for movie in recommended_movies])]

def recommend_movies_cb(user_id, ratings, movies, top_n=3):
    user_movies = ratings[ratings['user_id'] == user_id]['movie_id']
    user_genres = movies[movies['movie_id'].isin(user_movies)]['genre']
    combined_genres = ' '.join(user_genres)
    tfidf = TfidfVectorizer()
    genre_matrix = tfidf.fit_transform(movies['genre'])
    user_vector = tfidf.transform([combined_genres])
    similarities = cosine_similarity(user_vector, genre_matrix).flatten()
    movie_indices = similarities.argsort()[-top_n:][::-1]
    return movies.iloc[movie_indices]

if __name__ == "__main__":
    user_id = 1
    print("Collaborative Filtering Recommendations:")
    print(recommend_movies_cf(user_id, user_item_matrix, user_similarity_df, movies))
    print("\nContent-Based Filtering Recommendations:")
    print(recommend_movies_cb(user_id, ratings, movies))
