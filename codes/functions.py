from math import sqrt
import time


def isprime(num):
    """
    Returns true if num is prime
    """
    if num == 0 or num == 1 or not num % 2:
        if num == 2:
            return True
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


isprime(97)


def return_prime_till_n(n):
    """
    Returns a list of prime numbers till n
    """
    primes = [2]
    for i in range(3, n, 2):
        if isprime(i):
            primes.append(i)
    return primes


t0 = time.time()
print(len(return_prime_till_n(100000)))
t1 = time.time()
print(t1 - t0)


def prime_till_n(n):
    """
    Another method to return prime till n
    Needs modification
    """
    i = 2
    primes = list(range(2, n))
    while True:
        num = primes.index(i)
        for m in range(2, int(n / i) + 1):
            if i * m in primes:
                primes.remove(i * m)
            else:
                pass
        if i != primes[-1]:
            i = primes[num + 1]

        else:
            break
    return primes


def return_m_prime(m):
    """
    Returns mth prime
    """
    primes = [2]
    i = 1
    while len(primes) < m:
        i = i + 2
        if isprime(i):
            primes.append(i)
    return primes[m - 1]


# All above three functions use isprime() method


def factors(n):
    """
    Returns factors of n
    """
    factors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
            if i * i != n:
                factors.append(n / i)
    return factors
