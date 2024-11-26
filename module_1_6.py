my_dict = {'Ilya': 1999, 'Roma': 1996, 'Jenya': 1995, 'Olga': 1972}
print(my_dict)
print(my_dict.get('Ilya'))
print(my_dict.get('Oleg'))
my_dict.update({'Ivan': 1994,
                'Anton': 1988})
i = my_dict.pop('Ilya')
print(i)
print(my_dict)
my_set = {True, 'Anton', 5, 5, True, 55, 5}
print(my_set)
my_set.update({False, "Bus"})
my_set.remove(5)
print(my_set)
