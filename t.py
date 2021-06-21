print(list(str(123)))

mlist = [1, 2, 3, 4, 3, 4]
mlist.count(3)
mlist == list(set(mlist))
mlist[2]


def ispandigital(num):
    return list(str(num)) == list(set(list(str(num))))


for n in range(98765):
    for m in range(98765):
        num = n * m
        new_num = str(n) + str(m) + str(num)
        if ispandigital(int(new_num)) and num != 0:
            print(m, n, m * n)
