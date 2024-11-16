numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if i == 0:
        continue
    is_prime = False
    for j in range(len(numbers)):
        if j == 0:
            continue
        if numbers[i] % numbers[j] == 0 and numbers[j] != numbers[i]:
            is_prime = True
    if is_prime == False:
      primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes: ',primes)
print('Not Primes: ',not_primes)
