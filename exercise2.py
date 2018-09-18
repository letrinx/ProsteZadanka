def min_and_max(list):
    if any(list) != True:
        result = (None, None)  # Dzień dobry ! 15 linijka mi tak kazała
        return result
    minimum = min(list)
    maximum = max(list)
    result = (minimum, maximum)
    return result


print(min_and_max([3, 5, -3, 12, -2, 0]))  # zwróci (-3, 12)

print(min_and_max([12]))  # zwróci (12,12)

print(min_and_max([]))  # zwróci (None, None)
