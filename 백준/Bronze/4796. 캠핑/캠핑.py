i = 1
while True:
    total = 0
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    total += l * (v // p)
    if (v % p) > l: 
        total += l
    else:
        total += (v % p)
    print(f"Case {i}: {total}")
    i += 1 
    



