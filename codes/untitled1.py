
import time
from math import floor
t0 = time.time()
i = 9999
flage = True
while flage:
    tringular = []
    numbers = list(range(1,i))
    
    n = sum(numbers)
    print(n)
    divisors_n = []
    for m in range(1,floor(n/2)+1):
        if n%m == 0:
            divisors_n.append(m)
    if len(divisors_n)>=500:
        print(n)
        flage = False
    else:
        i+=1
        
    if i == 11000:
        flage = False
        
t1 = time.time()
print(t1-t0)