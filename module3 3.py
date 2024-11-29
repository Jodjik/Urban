def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params(1, 3, "False")
print_params(b = 25)
print_params(c = [1,2,3])
value_list = [2, 'не строка', False]
value_dict = {'a' : 2, 'b' : 'не строка', 'c' : False }
print_params(*value_list)
print_params(**value_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)