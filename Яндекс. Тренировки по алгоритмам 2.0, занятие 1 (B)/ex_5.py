def get_distance_to(coords, point):
	return ((coords[0] - point[0])**2 + (coords[1] - point[1])**2)**0.5

d = int(input())
coords = list(map(int, input().split(' ')))

if (coords[0] >= 0 and coords[1] >= 0 and coords[0] + coords[1] <= d):
	print(0)
else:
	dists = [0, 0, 0]
	dists[0] = get_distance_to((0, 0), coords)
	dists[1] = get_distance_to((d, 0), coords)
	dists[2] = get_distance_to((0, d), coords)
	if (dists[0] <= dists[1]):
		if (dists[0] <= dists[2]):
			print(1)
		else:
			print(3)
	elif (dists[1] <= dists[2]):
		print(2)
	else:
		print(3)
