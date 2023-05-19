def evennot(a):
    ch = 0
    nech = 0
    kch = 0
    knechet = 0
    for s in range(len(a)):
        if a[s] % 2 == 0:
            kch += 1
            ch = a[s]
        else:
            knechet += 1
            nech = a[s]
    if kch < knechet:
        return ch
    else:
        return nech
    
print(evennot([int(i) for i in input().split()]))
