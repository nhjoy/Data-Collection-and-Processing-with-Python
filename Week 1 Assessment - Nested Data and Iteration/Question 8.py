# Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.


l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []

for elements in l_of_l:
    for element in elements[2:3]:
        third.append(element)
print(third)