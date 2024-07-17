import random
n = random.randint(3,20)
print(n)
password = ''
for k in range(1, 20):
    for j in range(1, 20):
        if not n % (k + j) and k < j:
            password = password + str(k) + str(j)
print(password)