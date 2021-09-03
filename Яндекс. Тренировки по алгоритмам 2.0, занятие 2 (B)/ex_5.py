input()
folders = list(map(int, input().split()))

folders.remove(max(folders))
print(sum(folders))
