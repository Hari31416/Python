def old_macdonald(name):
    name_new = ''
    letters_new = []
    for n in range(0, len(name)-1):
        if n == 0 or n == 3:
            capital = name[n].upper
            letters_new.append(capital)
        else:
            letters_new.append(name[n])
    for letter in letters_new:
        name_new = name_new + letter
    return name_new
new = old_macdonald('macdonald')
print(new)