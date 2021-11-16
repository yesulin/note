def test():
    num=10
    def test_in():
        nonlocal num
        num=10+10

    test_in()
    print(num)
test()