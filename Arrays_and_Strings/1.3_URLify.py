def urlify1(string) -> str:
    return string.strip().replace(' ', '%20')


def urlify2(string) -> str:
    SPACE = ' '
    URL_SPACE = '%20'
    string_list = [x for x in string.rstrip()]
    for i in range(len(string_list)):
        if string_list[i] == SPACE:
            string_list[i] = URL_SPACE
    return ''.join(string_list)

print(urlify1('test sentence test  '))
print(urlify2('test sentence test  '))
