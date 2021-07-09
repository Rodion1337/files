def arrange(s):
    t = c = []
    c = s.copy()
    while len(c) > 0:
        t.append(c.pop(0))
        if len(c) > 0:
            t.append(c.pop(-1))
            c.reverse()
    return(t)


def arrange2(s):
    t = c = []
    c = s.copy()
    while len(c) > 0:
        if len(c) > 1:
            t.append(c.pop(0))
            print(s, c, t)
            t.append(c.pop(-1))
            print(s, c, t)
        if len(c) > 1:
            t.append(c.pop(-1))
            print(s, c, t)
            t.append(c.pop(0))
            print(s, c, t)
        if len(c) == 1:
            t.append(c.pop(0))
            print(s, c, t)
    return(t)


def arrange3(s):
    t = c = []
    c = s.copy()
    while len(c) > 0:
        while len(c) > 3:
            t.append(c.pop(0))
            t.append(c.pop(-1))
            t.append(c.pop(-1))
            t.append(c.pop(0))
        if len(c) > 1 and len(c) <= 3:
            t.append(c.pop(0))
            t.append(c.pop(-1))
        if len(c) == 1:
            t.append(c.pop(0))
    return(t)



def arrange4(s):
    t = c = []
    x = 1
    c = s.copy()
    for x in range(1, len(c) + 1):
        if len(c) >= 4:
            t.append(c.pop(0))
            t.append(c.pop(-1))
            t.append(c.pop(-1))
            t.append(c.pop(0))
            x -= 1
        if len(c) > 1 and len(c) < 4:
            t.append(c.pop(0))
            t.append(c.pop(-1))
            x -= 1
        if len(c) == 1:
            t.append(c.pop(0))
            x -= 1
    return(t)
