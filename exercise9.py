from random import randint


def domino(count):
    list = []
    i = 0
    while (i < count):
        i += 1
        x = randint(0, 6)
        y = randint(0, 6)
        list.append(str(y) + "-" + str(x))
    return list


print(domino(3)) # Zwróci np ['2-1', '0-3', '5-6']
