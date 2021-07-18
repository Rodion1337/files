import random

def generate_color_rgb():
    r = '%x' % (random.randrange(0, 255))
    g = '%x' % (random.randrange(0, 255))
    b = '%x' % (random.randrange(0, 255))
    x = '#'
    if len(r) < 2:
        x = x + '0' + r
    else:
        x += r

    if len(g) < 2:
        x = x + '0' + g
    else:
        x += g

    if len(b) < 2:
        x = x + '0' + b
    else:
        x += b

    return(x)
