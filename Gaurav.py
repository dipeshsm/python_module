

def MaxWordLen(filename):
    words = filename.split()
    MaxLen = 0
    for i in words:
        if len(i) > MaxLen:
            MaxLen = len(i)
            longList = [i]
        elif len(i) == MaxLen:
            longlist.append(i)
    for j in longlist:
        print(j)

