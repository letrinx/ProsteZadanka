def multiply_list(list, num):
    result = []
    for element in list:
        result.append(element * num)
    return result


print(multiply_list([3, 5, 2, 6], 2))
# zwróci [6,10,4,12]
