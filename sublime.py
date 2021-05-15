import math
def prime(num):
    multiples = []
    final_num = math.floor(num**0.5)
    for i in range(2, final_num+1):
      if num%i ==0:
        multiples.append(i)
    return len(multiples) == 1

def count_primes(num_range):
    primes = []
    for m in list(range(2, nu+1, 2)):
        if prime(m):
            primes.append(m)
    return len(primes)
num_primes = count_primes(140000)
print(num_primes)

