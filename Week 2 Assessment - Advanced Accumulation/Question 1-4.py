# Question 1

'''
Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” 
to the beginning of each element using mapping.
'''


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map(lambda str: "Fruit: " +str, lst_check)



# Question 2

'''
Below, we have provided a list of strings called countries. 
Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.
'''

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = filter(lambda country: 'B' in country, countries)


#Question 3

'''
Below, we have provided a list of tuples that contain the names of Game of Thrones characters. 
Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
'''

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [name[1] for name in people]

# Question 4

'''
Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
'''

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2 = [l*2 for l in lst]