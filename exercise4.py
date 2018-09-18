def split_list(list):
    firstList = list[::2]
    secondList = list[1::2]
    result = (firstList, secondList)
    return result


print(split_list([1, 3, 5, 7, 10, 11, 12, 13]))  # Zwróci ([1,5,10,12], [3,7,11,13])
