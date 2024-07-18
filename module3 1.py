def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    print(result)
def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if string.lower() == i.lower():
            flag = True
    print(flag)

calls = 0
x = 'Автобус'
string_info(x)
x = 'Задачка'
string_info(x)
j = 'авто'
k = ['автобус', 'АВТОМОБИЛЬ', 'автоинспектор', 'машина', 'АВТО']
is_contains(j, k)
j = 'Урок'
k = ['Рок', 'Курок', 'Придурок', 'Шнурок', 'Сурок']
is_contains(j, k)
print(calls)