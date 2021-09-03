n, i, j = map(int, input().split(' '))

if (i > j):
	i, j = j, i

if (n - j + i - 1 >  j - i - 1):
	print(j - i - 1)
else:
	print(n - j + i - 1)
