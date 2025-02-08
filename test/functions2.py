movies = [
{ "name": "Usual Suspects",  "imdb": 7.0, "category": "Thriller" },
{ "name": "Hitman", "imdb": 6.3, "category": "Action" },
{ "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" },
{ "name": "The Help", "imdb": 8.0, "category": "Drama" },
{ "name": "The Choice", "imdb": 6.2, "category": "Romance" },
{ "name": "Colonia", "imdb": 7.4, "category": "Romance" },
{ "name": "Love", "imdb": 6.0, "category": "Romance" },
{ "name": "Bride Wars", "imdb": 5.4, "category": "Romance" },
{ "name": "AlphaJet", "imdb": 3.2, "category": "War" },
{ "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" },
{ "name": "Joking muck", "imdb": 7.2, "category": "Comedy" },
{ "name": "What is the name", "imdb": 9.2, "category": "Suspense" },
{ "name": "Detective", "imdb": 7.0, "category": "Suspense" },
{ "name": "Exam", "imdb": 4.2, "category": "Thriller" },
{ "name": "We Two", "imdb": 7.2, "category": "Romance" }]

def highly_rated(movie):
    return movie["imdb"] > 5.5
print(highly_rated(movies[2]))


def h_r_movies(movies):
    result = []
    for movie in movies:
        if highly_rated(movie):
            result.append(movie)
    return result
print(h_r_movies(movies))


def movies_category(movies, category):
    result = []
    for movie in movies:
        if movie["category"].lower() == category.lower():
            result.append(movie)
    return result
print(movies_category(movies, "Romance"))


def average_imdb(movies):
    if not movies:
        return 0
    total = 0
    count = 0
    for movie in movies:
        total += movie["imdb"]
        count += 1
    return total / count
print(average_imdb(movies))


def imdb_score_by_category(movies, category):
    category_movies = movies_category(movies, category)
    return average_imdb(category_movies)
print(imdb_score_by_category(movies, "Romance"))