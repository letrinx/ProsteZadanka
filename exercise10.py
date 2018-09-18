def domino_tuple(list):
    tuplelist = []
    for element in list:
        tup = (int(element[0]),int(element[2]))
        tuplelist.append(tup)
    return tuplelist

print(domino_tuple(['2-1', '0-3', '5-6'])) # zwróci [(2,1), (0,3), (5,6)]