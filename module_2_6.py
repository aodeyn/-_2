def parole():
    n = 0
    n = int(input('Введите число:'))+1
    for i  in range(n) :
        string= str(i) + ' - '
        if i < 3 :
            continue
        list_j = []
        for j in range(n):
            if j < 1:
                continue
            for k in range(n):
                if k < 1:
                    continue
                m = j + k
                if i % m == 0 and j != k:
                    if k in  list_j:
                        continue
                    list_j.append(j)
                    string = string + str(j) + str(k)
                    continue
        print(string)
parole()


