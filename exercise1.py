def sum_range(min, max):
    result = 0
    for number in range(min, max + 1):
        result += number
    return result


print(sum_range(2, 5))
print(sum_range(-2, 2))
