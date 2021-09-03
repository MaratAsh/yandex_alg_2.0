x, y, z = map(int, input().split(' '))

if (x > 12 and y <= 12 or x <= 12 and y > 12 or x == y and x <= 12):
	print(1)
else:
	print(0)
