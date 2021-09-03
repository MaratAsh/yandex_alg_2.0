max_num = 0
max_cnt = 0

while True:
	n = int(input())
	if (n == 0):
		break
	if (max_num < n):
		max_num = n
		max_cnt = 1
	elif (max_num == n):
		max_cnt += 1
print(max_cnt)
