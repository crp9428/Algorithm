def getDecompose(n):
    const = n
    while(n // 10 > 0):
        const += n % 10
        n = n // 10
    const += n
    return const

n = int(input().strip())
consts = set()

for i in range(1, n+1):
    dec = getDecompose(i)
    if dec == n:
        consts.add(i)

print("%d\n" % min(consts)) if len(consts) > 0 else print("0")