import json
import math
from numpy import random

movie_file = 'IMDb_movies.json'
ratings_file = 'IMDb_ratings.json'
user_file = 'users.json'

# serialize movie fixtures
serialized_movies = []
with open(movie_file) as m:
    movies = json.load(m)
    for field in movies:
        tmp = {}
        tmp['model'] = "movies.Movie"
        tmp['pk'] = field["id"]
        del field['id']
        tmp['fields'] = field
        serialized_movies.append(tmp)

with open('fixtures/movies.json', 'w') as f:
    json.dump(serialized_movies, f, indent=2, ensure_ascii=False)
    
# serialize rating fixtures
serialized_ratings = []    
with open(ratings_file) as r:
    with open(user_file) as u:
        ratings = json.load(r)
        users = json.load(u)
        counter = 1
        for field in ratings:
            movie = field["id"]
            n = round(1 + field["number"]/10)
            mean = field["rating"]
            for i in range(n):
                tmp = {}
                tmp['model'] = "movies.Rating"
                tmp['pk'] = counter
                counter += 1
                fields = {}
                fields["movie"] = movie
                fields["user"] = users[math.floor(random.random()*len(users))]["pk"]
                rand = math.floor(random.normal(loc=mean, scale=1))
                fields["num_rating"] = min(rand, 10)
                tmp['fields'] = fields
                serialized_ratings.append(tmp)

with open('fixtures/ratings.json', 'w') as f:
    json.dump(serialized_ratings, f, indent=2, ensure_ascii=False)

print(counter)