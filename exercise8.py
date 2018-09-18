def policz_kotki(text):
    list = text.split()
    result = 0
    for element in list:
        if "kot" in element.lower():
            result += 1
    return result


print(policz_kotki('Kotara to nie kotek, ale kotkiem jest Filemon'))
