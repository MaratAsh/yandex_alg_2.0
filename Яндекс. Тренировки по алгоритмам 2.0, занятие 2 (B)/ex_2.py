def get_max_len_(b):
	for i in range(len(b)):
		if (b[i] == 2):
			return i
	return 0

def get_max_len(b):
	max_len = 0
	for i in range(len(b)):
		if (b[i] == 1):
			len_l = get_max_len_(b[i::-1])
			len_r = get_max_len_(b[i::])
			if len_l == 0:
				if (max_len < len_r):
					max_len = len_r
			elif len_r == 0:
				if (max_len < len_l):
					max_len = len_l
			elif (max_len < min(len_r, len_l)):
				max_len = min(len_r, len_l)
	return max_len
			

buildings = list(map(int, input().split()))

print(get_max_len(buildings))
