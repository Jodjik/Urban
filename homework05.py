immutable_var = (1, True, 'bus', 4, 5)
print(immutable_var)
print(type(immutable_var)) #Проверял себя
print(type(immutable_var[0]))
#immutable_var[0] = immutable_var[0] + 1
#Кортеж не поддерживает обращения к элементам и используется только для хранения информации
print(immutable_var[0])
mutable_list = [1, True, 'bus', 4, 5]
mutable_list[0] = mutable_list[0] + 10
mutable_list.remove('bus')
mutable_list.append('car')
mutable_list.reverse()
print(mutable_list)