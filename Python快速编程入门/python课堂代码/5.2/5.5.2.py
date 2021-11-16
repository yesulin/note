ls=[1,2,3,4,5,6]
l=[data*data for data in ls ] # 列表推导式
s={data*data for data in ls}
print(l)
print(s)