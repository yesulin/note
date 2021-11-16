ls=[1,2,3,4,5,6,7,8,9]
ls=[data*data  for data in ls ]
print(ls)

# ls=[1,2,3,4,5,6,7,8,9]
# for data in ls:
#     sum=data*data
#     print(sum,end=' ')

ls=[1,2,3,4,5,6,7,8,9]
ls=[data for data in ls if data>4]
print(ls)

ls_one=[1,2,3]
ls_two=[3,4,5]
ls_three=[x+y for x in ls_one for y in ls_two]
print(ls_three)

ls_one=[1,2,3]
ls_two=[3,4,5]
for x in ls_one:
    for y in ls_two:
        print(x+y,end=' ')

