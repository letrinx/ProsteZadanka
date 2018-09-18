def count_character(text, letter):
    result = 0
    for l in text:
        if l.upper() == letter.upper():
            result += 1

    return result

def count_all_characters(text):
    result = {}
    for letter in text:
        if letter.lower() not in result:
            result.update({letter.lower(): count_character(text, letter)})
    return result


print(count_all_characters('Mam dzisiaj dobry humor'))

""" Zwróci
{
    'm': 3,
    'a': 2,
    ' ': 3,
    'd': 2,
    'z': 1,
    'i': 2,
    's': 1,
    'j': 1,
    'o': 2,
    'b': 1,
    'r': 2, ---- Jakiś błąd się wkradł, dwa razy r
    'y': 1,
    'h': 1,
    'u': 1,
    'r': 1, ----
}
"""
