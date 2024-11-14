n = 0
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
m = len(my_list)
while n <= my_list[len(my_list)-m] and m > 0:
    print(my_list[len(my_list)-m])
    m-=1
    continue
    break