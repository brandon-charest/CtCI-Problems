import unittest

# Assume ASCII characters


# with data structure
def is_unique(string) -> bool:
    if len(string) > 128:
        return False
    letters = set()
    for ch in string:
        if ch not in letters:
            letters.add(ch)
        else:
            return False
    return True

# def is_unique(string) -> bool:
#     if len(string) > 128:
#         return False
#
#     for i in range(len(string)):
#         for j in string[i+1:]:
#             if string[i] == j:
#                 return False
#     return True


#
# strings = ['abcd', 'racecar', 'world', 'hello', 'hevloh']
# for s in strings:
#     print(f'{s}: {is_unique(s)}')

class Test(unittest.TestCase):
    test_true = ['acbdefg', '1/*fs[pz', 'world', '']
    test_false = ['1231', 'hello', '-=+12plmandfgt**']
    def test_unique(self):
        for test_string in self.test_true:
            result = is_unique(test_string)
            self.assertTrue(result)
        for test_string in self.test_false:
            result = is_unique(test_string)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()