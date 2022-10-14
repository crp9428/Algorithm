def power5(n):
    count = 0
    while(n >= 5):
        count += (n // 5)
        n //= 5
    return count

def power2(n):
    count = 0
    while(n >= 2):
        count += (n // 2)
        n //= 2
    return count

N, K = map(int, input().strip().split())
print(f"{min((power5(N) - power5(N-K) - power5(K)), (power2(N) - power2(N-K) - power2(K)))}")