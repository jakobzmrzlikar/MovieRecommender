import csv
import json

csv_file = 'IMDb_movies.csv'
movie_file = 'IMDb_movies.json'
ratings_file = 'IMDb_ratings.json'

movie_list = []
ratings_list = []

with open(csv_file, 'r') as in_file:
    reader = csv.reader(in_file)
    fields = next(reader)
    for i, row in enumerate(reader):
        rating = {}
        movie = {}
        rating["id"] = int(row[0][2:])
        rating["rating"] = float(row[14])
        rating["number"] = int(row[15])
        for field, value in zip(fields[:10], row[:10]):
            if field == "imdb_title_id":
                movie["id"] = int(value[2:])
            elif field == "date_published":
                if len(value) < 10:
                    value += "-01-01"
                movie["date_published"] = value
            else:
                movie[field] = value
        movie_list.append(movie)
        ratings_list.append(rating)

with open(movie_file, 'w') as out_file:
    out_file.write(json.dumps(movie_list, indent=2, ensure_ascii=False))

with open(ratings_file, 'w') as out_file:
    out_file.write(json.dumps(ratings_list, indent=2, ensure_ascii=False))
