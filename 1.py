hashtag = input().split()
tag = '#'

if len(hashtag) < 140 and len(hashtag) != 0:
    for s in hashtag:

        tag += s.title()

    print(tag)

else:

    print(False)

