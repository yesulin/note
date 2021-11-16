def test(*args):  # 接收以元组形式打包的多个值
    print(args)


print(11, 22, 33, 44, 55)


def test_dic(**kwargs):  # 接收以字典形式打包的多个值
    print(kwargs)


test_dic(a=11, b=22, c=33, d=44, e=55)
