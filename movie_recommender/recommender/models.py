from django.conf import settings
from django.db.models import Count, Avg


from surprise import SVD, Reader, Dataset, dump
from surprise.model_selection import train_test_split, cross_validate

import pandas as pd

import json

from movies.models import Movie, View, Rating

data_file = '../data/train_data.json'


class CollaborativeFilteringRecommender(object):

    def __init__(self):
        self.algorithm = SVD()
        

    def save(self):
        name = "/model_snapshots/SVD.dump"
        file = settings.BASE_DIR + name
        dump.dump(file, algo=self.algorithm)
        print("Saving model snapshot for algorithm SVD")


    def load(self, file):
        _, algorithm = dump.load(file)
        self.algorithm = algorithm


    def train(self):
        with open(data_file) as f:
            ratings = json.load(f)
        df = pd.DataFrame(ratings)
        reader = Reader(rating_scale=(1, 10))
        data = Dataset.load_from_df(df, reader)
        trainset = data.build_full_trainset()
        # trainset, testset = train_test_split(data, test_size=0.25)

        self.algorithm.fit(trainset)
        
        # test = self.algorithm.test(testset)
        # cross_validate(self.algorithm, data, cv=5, verbose=True)
        
        self.save()


    def recommend(self, user_id, threshold=7):
        movie_lst = Movie.objects.all().values_list('id')
        recommended = []
        for movie_id in movie_lst:
            rating = self.algorithm.predict(user_id, movie_id)[3]
            if rating > threshold:
                recommended.append(movie_id)
        return recommended


class TopRatedRecommender(object):

    def __init__(self):
        pass

    
    def recommend(self, user_id, n=10):
        top_rated = Rating.objects.order_by('-num_rating')[:n]
        return [rating['movie'] for rating in top_rated]


class MostViewedRecommender(object):

    def __init__(self):
        pass


    def recommend(self, user_id, n=10):
        movies = []
        most_viewed = View.objects.values_list('movie').annotate(count=Count('movie')).order_by('-count')[:n]
        for id, num in most_viewed:
            movies.append(Movie.objects.filter(id=id)[0])
        return movies
