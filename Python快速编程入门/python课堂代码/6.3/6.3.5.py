def test(a, b, c=33, *args, **kwargs):
    # 位置参数，关键字参数，默认参数，元组打包，字典打包
    print(a, b, c, args, kwargs)

test(1,2)
test(1,2,3)
test(1,2,3,4)
test(1,2,3,4,e=5)