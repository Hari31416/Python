from math import sqrt
def isprime(num):
    if num == 0 or num == 1 or not num % 2:
        if num == 2:
            return True
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def return_prime_till_n(n):
    primes =[2]
    for i in range(3, n, 2):
        if isprime(i):
            primes.append(i)
    return primes

import time
t0 = time.time()
primes = return_prime_till_n(3000000)
t1 = time.time()
print(sum(primes))
print(t1-t0)