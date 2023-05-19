# 10870_피보나치수5

def fibo(N):
    if N <= 1:
        return N

    return fibo(N - 1) + fibo(N - 2)

n = int(input())
ans = fibo(n)

print(ans)