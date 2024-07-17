numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True #На начале 4-го пункта задачи у меня наччались сложности, вообще не понял про Flag и как пользоваться
for j in numbers: #В связи с этим подгонял свое выполнение под пункты как мог, строки 4 и 7 можно удалить
    for i in range(len(numbers)):
        is_prime = numbers[i] == j
        if i == 0 or j == 1 or numbers[i] > j:
            continue
        elif is_prime: #numbers[i] == j
            prime.append(j)
            #print(f'j % numbers[i] p {j % numbers[i]} {j} {numbers[i]}') #Эти строки помогали отслеживать какие
        elif j % numbers[i] == 0:                                       #значения и в какой момент принимают
            not_prime.append(j)                                         #переменные
            #print(f'j % numbers[i] np {j % numbers[i]} {j} {numbers[i]}')
            break
print(f'primes: {prime}')
print(f'not_primes: {not_prime}')