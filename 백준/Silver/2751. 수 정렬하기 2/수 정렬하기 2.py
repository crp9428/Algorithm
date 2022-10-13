import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

# 병합정렬
def mergeSort(list, p, q):
    if p >= q: 
        return
    mid = (p + q) // 2
    mergeSort(list, p, mid)
    mergeSort(list, mid+ 1, q)
    merge(list, p, mid + 1, q)

def merge(list, left, right, end):
    merged = []
    l, r = left, right
    while l < right and r <= end:
        if list[l] <= list[r]:
            merged.append(list[l])
            l +=1
        else:
            merged.append(list[r])
            r +=1
    while l < right:
        merged.append(list[l])
        l +=1
    while r <= end:
        merged.append(list[r])
        r+=1

    l = left
    for n in merged:
        list[l] = n	
        l +=1

mergeSort(arr, 0, len(arr) - 1)

for v in arr:
    print(f"{v}\n")