# Question 5

'''
Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. 
Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
'''

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [name[0] for name in students if name[1]>=70]

# Question 6

'''
Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if 
they are both longer than 3 characters each.
'''

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3 = zip(l1, l2)
opposites = filter(lambda x: len(x[0])>3 and len(x[1])>3, l3)

# Question 7

'''
Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. 
From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
'''

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = zip(species, population)

endangered = [save[0] for save in pop_info if save[1]<2500]