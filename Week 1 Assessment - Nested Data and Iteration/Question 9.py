'''
Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. 
If it does not contain the letter “t”, save the athlete name into list other.
'''

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for players in athletes:
    for names in players:
        if 't' in names:
            t.append(names)
        else:
            other.append(names)
        
    