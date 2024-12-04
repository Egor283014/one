numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []         # простые числа
not_primes = []     # не простые числа.
for n in numbers[1:]:
    for d in range(2,n):
       if n % d == 0:
           print(n,' не простое')
           not_primes.append(n)
           break
    else:
        print(n,'простое')
        primes.append(n)
