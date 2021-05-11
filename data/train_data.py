import json
import random

ratings_dict = {
    'itemID': [],
    'userID': [],
    'rating': []
}

with open('IMDb_ratings.json') as f:
    ratings = json.load(f)
    for rating in ratings:
        ratings_dict['itemID'].append(rating['id'])
        ratings_dict['userID'].append(random.randint(1, 10000))
        ratings_dict['rating'].append(rating['rating'])

with open('train_data.json', 'w') as f:
    json.dump(ratings_dict, f, indent=2, ensure_ascii=False)
