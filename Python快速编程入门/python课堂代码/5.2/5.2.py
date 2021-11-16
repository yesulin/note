t1=()
t2=(1,)
t3=(1,2,3)
t4=(1,'c',('e',2))
print(t4)

t5=tuple()
t6=tuple([1,2,3])
t7=tuple('python')
print(t5,t6,t7)

t8=(1,2,3,4,'a','c',3.14)
print(t8[1])
print(t8[2:4])
for data in t8:
    print(data,end=' ')
