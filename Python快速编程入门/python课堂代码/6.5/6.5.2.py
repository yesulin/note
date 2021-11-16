num=10
def test():
    global num #通过 global 声明为全局变量
    num=num+2
    print(num)
test()
print(num)