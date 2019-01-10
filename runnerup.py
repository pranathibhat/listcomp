n = int(input())
arr = (map(int, input().split()))
arr.remove(max(arr))
print(max(arr))