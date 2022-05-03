def base64_to_base10(str):
    a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    b = 0
    c = list(str)
    print(c)
    if len(c) == 1:
        return (a.index(c[-1]))
    elif len(c) == 2:
        return(a.index(c[-1]) + (64 * a.index(c[-2])))
    elif len(c) == 3:
        return(((64 ** 2) * a.index(c[-3])) + a.index(c[-1]) + (64 * a.index(c[-2])))

def base64_to_base10_2(str):
    a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    b = result = 0
    c = list(str)
    c.reverse()
    print(c)
    if len(c) == 1:
        return (a.index(c[-1]))
    else:
        while b < (len(c) - 1):
            result  += 64 ** (b + 1) * a.index(c[(b + 1)])
            print(result, b)
            b += 1
        return(result + a.index(c[0]))