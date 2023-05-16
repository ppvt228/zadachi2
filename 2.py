def first_non_repeating_letter(a):
    b = [0] * len(a)
    c = '""'
    for s in range(len(a)):
        b[s] = a[s:s + 1]
    for s in b:
        if ((b.count(s.upper())) == 1 and (b.count(s.lower())) == 0) or ((b.count(s.upper())) == 0 and (b.count(s.lower())) == 1):
            c = s
            break
    return(c)

print(first_non_repeating_letter(input()))
