#删除指定字符
old_str='  life is short,use python   '
print('原始字符:',old_str)
print(f'strip方法:{old_str.strip()}') #左边和右边
print(f'lstrip方法:{old_str.lstrip()}') #左边
print(f'rstrip方法:{old_str.rstrip()}') #右边

#大小写转换
str='hello woRld'
print(f'全部转换成大写：{str.upper()}')
print(f'全部转换成小写：{str.lower()}')
print(f'首字母转换在大写：{str.capitalize()}')
print(f'第个单词首字母转换在大写：{str.title()}')

#字符串对齐
str1='hello world'
print(f"居中对齐：{str1.center(13,'-')}")
print(f"左对齐：{str1.ljust(13,'+')}")
print(f"右对齐：{str1.rjust(13,'+')}")