def split(string_sep, separators):
    res = []
    last = 0  # the last position of an separators
    index = 0
    for index, char in enumerate(string_sep):
        if char in operators:
            res.append(string_sep[last:index].strip())  # strip if you dont want space enter separtors and words
            res.append(char)
            last = index + 1  # +1 to not take the separator

    # for the last add to the list
    if last <= index:
        res.append(string_sep[last:])
    return res


operators = ["+", "-", "*"]
string_sep = "three hundred + four - fifty six * eight"

print(split(string_sep, operators))
