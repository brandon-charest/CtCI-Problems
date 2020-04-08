def check_permutation(string1, string2) -> bool:

    if string1.isnumeric() or string2.isnumeric():
        return False

    if len(string1) is not len(string2):
        return False

    sorted_string1 = sorted(string1.lower())
    sorted_string2 = sorted(string2.lower())

    for i in range(len(string1)):
        if sorted_string1[i] != sorted_string2[i]:
            return False
    return True


test1 = ['God', 'Dog']
test2 = ['Top', 'Pat']

print(check_permutation(test1[0], test1[1]))
print(check_permutation(test2[0], test2[1]))
