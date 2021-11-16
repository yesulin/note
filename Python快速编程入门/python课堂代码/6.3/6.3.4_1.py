def test(a, b, c, d, e):
    print(a, b, c, d, e)


num = (1, 2, 3, 4, 5)
test(*num)


def test_dic(a, b, c, d, e):
    print(a, b, c, d, e)


nums = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
test_dic(**nums)
