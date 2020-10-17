
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

import requests_with_caching
import json

def get_movie_data(movie):
    url = 'http://www.omdbapi.com/'
    
    params= {}
    params['t'] = movie
    params['r'] = 'json'
    
    resp = requests_with_caching.get(url, params = params)

    return resp.json()

#print(get_movie_data("Baby Mama"))

def get_movie_rating(movies):
    ratings = movies['Ratings']
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'][:-1])
    return 0
print(get_movie_rating(get_movie_data("Deadpool 2")))