# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    url = 'https://tastedive.com/api/similar'
    
    params= {}
    params['q'] = movie
    params['type'] = 'movies'
    params['limit'] = 5
    
    tastedive_resp = requests_with_caching.get(url, params = params)

    return tastedive_resp.json()

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")