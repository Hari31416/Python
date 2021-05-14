def count_primes(num):
    the_tuple = []
    for n in range(2, num):
        for m in range(2, num):
            divisors = []
            if n%m == 0:
                divisors.append(m)
count_primes(100)
count = [(n,m) for n in range(2,101) m in range(2, 102) if n%m ==0]
print(count)
