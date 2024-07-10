my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while my_list[0] >= 0:
    if my_list[0] > 0:
        print(my_list[0])
        del my_list[0]
        continue
    elif my_list[0] == 0:
        del my_list[0]
    else:
        break