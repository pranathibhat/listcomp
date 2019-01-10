n = int(input())
arr = list(map(int, input().split()))
z=max(arr)
while z==max(arr):
	arr.remove(max(arr))
print(max(arr))