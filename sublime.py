import time
t0 = time.time()
i = 3
flage = True
while flage:
    tringular = []
    numbers = list(range(1,i))
    for n in range(1,i):
        tringular.append(sum(numbers[0:n]))
    n = tringular[i-2]
    divisors_n = []
    for m in range(1,n+1):
        if n%m == 0:
            m = m/n
            divisors_n.append(m)
    if len(divisors_n)==50:
        print(n)
        flage = False
    else:
        i+=1

t1 = time.time()
print(t1-t0)