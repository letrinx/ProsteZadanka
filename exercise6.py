def count_character(text, letter):
    result = 0
    for l in text:
        if l.upper() == letter.upper():
            result += 1

    return result


print(count_character('Mam dzisiaj dobry humor', 'm'))
# zwróci 3
