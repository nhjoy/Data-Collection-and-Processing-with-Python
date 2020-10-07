# Question: Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. 
# See comments for further instructions.


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

# solution

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = 'yellow' in lst[2]

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst[1]

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = 'orange' in lst[0]
