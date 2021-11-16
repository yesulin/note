def fib_recur(n):
	if n <= 1:
		return n
	else:
		return fib_recur(n-1) + fib_recur(n-2)
print('斐波那契数列:',end='')
for i in range(1, 20):
	print(fib_recur(i), end=' ')