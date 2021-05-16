from math import floor

def is_prime(num):
    #function to check if a number is prime
    num_range = floor(num**0.5 + 1)
    divisors = [n for n in range(2, num_range) if num%n==0]
    return len(divisors) == 0

def return_prime(n):
    primes = [n for n in range(2, n) if is_prime(n)]
    return primes[10000]

number = return_prime(105000)
print(number)
