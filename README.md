# MovieRecommender

A (very simple) movie search and recommendation web app based on Django.

## Usage
Before starting the appliaction, you have to install all dependencies. 
For installing them in a seperate virtual enviornment (strongly recommended), run the code below:

```
python -m virtualenv <enviornment name>
source <enviornment name>/bin/activate
pip install -r requirements.txt
```

After installing all required dependencies, simply navigate to the project directory and run the Django server:

```
cd movie_recommender/
python  manage.py runserver
```

## Online demo
An online demo version running on [Binder](https://mybinder.org/) is also available [here](https://mybinder.org/v2/gh/jakobzmrzlikar/MovieRecommender/main?urlpath=proxy/8000/).