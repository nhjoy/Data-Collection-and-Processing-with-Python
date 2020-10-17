
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
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
#print(get_movies_from_tastedive("Bridesmaids"))

def extract_movie_titles(data):
    name = [x['Name'] for x in data['Similar']['Results']]
    return name
#print(extract_movie_titles(get_movies_from_tastedive("Bridesmaids")))
def get_related_titles(movies):
    lst = []
    for movie in movies:
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(lst))

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

def get_sorted_recommendations(movie_lst):
    dict2 = {}
    for title in get_related_titles(movie_lst):
        dict2[title] = get_movie_rating(get_movie_data(title))
    return [x[0] for x in sorted(dict2.items(), key=lambda item: (item[1], item[0]), reverse=True)]