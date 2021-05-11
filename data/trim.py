import json

with open("fixtures/ratings.json") as f:
    ratings = json.load(f)
    with open("fixtures/ratings_small.json", 'w') as g:
        json.dump(ratings[:1000], g, indent=2, ensure_ascii=False)
