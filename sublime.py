def factors(num):
    factors = []
    for n in range(1, num+1):
        if num%n==0:
            factors.append(n)
    return len(factors)

import time
t0 = time.time()
print(factors(27494820))
t1 = time.time()
print(t1-t0)