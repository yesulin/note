num=10 # 全局变量
def test_1():
    print(num) # 可以访问全局变量
        # num=num+1 不能修改全局变量

test_1()

print(num)