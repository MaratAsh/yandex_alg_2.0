l, k = map(int, input().split()[:2])
params = list(map(int, input().split()[:k]))

if (l % 2 == 1 and l // 2 in params):
	print(l // 2)
else:
	l_2 = l // 2
	while True:
		if (params[0] < l_2 and params[1] < l_2):
			params.remove(params[0])
		else:
			break
	print(params[0], params[1])
