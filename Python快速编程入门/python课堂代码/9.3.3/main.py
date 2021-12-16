def get_width():
    print("get_width开始执行")
    num=int(input("请输入除数："))
    width_len=10/num
    print("get_width执行结束")
    return width_len
def calc_area():
    print('calc_area开始结束')
    width_len=get_width()
    print('calc_area执行结束')
    return width_len*width_len
def show_area():
    try:
        print('show_area开始执行')
        area_val=calc_area()
        print(f'正方形的面积是：{area_val}')
        print('show_area执行结束')
    except ZeroDivisionError as e:
        print(f'捕捉到异常：{e}')
show_area()