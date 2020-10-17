
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

import requests_with_caching
import json

def get_movie_data(movie):
    url = 'http://www.omdbapi.com/'
    
    params= {}
    params['t'] = movie
    params['r'] = 'json'
    
    resp = requests_with_caching.get(url, params = params)

    return resp.json()