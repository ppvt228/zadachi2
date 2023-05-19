def split(a):
    b = []
    for i in range(0, len(a), 2):
        if i + 1 < len(a):
            b.append(a[i:i + 2])
        else:
            b.append(a[i] + '_')
    return b
print(split(input()))
