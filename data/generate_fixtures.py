import json
import math
from numpy import random

movie_file = 'IMDb_movies.json'
ratings_file = 'IMDb_ratings.json'
user_file = 'users.json'

used_ids = set()

# serialize movie fixtures
serialized_movies = []
with open(movie_file) as m:
    movies = json.load(m)
    random.shuffle(movies)
    movies = movies[:1000]
    for field in movies:
        tmp = {}
        tmp['model'] = "movies.Movie"
        tmp['pk'] = field["id"]
        used_ids.add(field["id"])
        del field['id']
        tmp['fields'] = field
        serialized_movies.append(tmp)

with open('fixtures/movies.json', 'w') as f:
    print("dumping movies into fixtures/movies.json")
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
            if movie not in used_ids:
                continue
            n = round(1 + field["number"]/10)
            n = min(n, 1000)
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
                rand = min(max(1, rand), 10)
                fields["num_rating"] = rand
                tmp['fields'] = fields
                serialized_ratings.append(tmp)

with open('fixtures/ratings.json', 'w') as f:
    print("dumping ratings into fixtures/ratings.json")
    json.dump(serialized_ratings, f, indent=2, ensure_ascii=False)
