def fib_fast(n):
    if n <= 1:
        return n
    a = [0, 1]
    while True:
        a.append((a[-1]+a[-2]) % 10)
        if a[-1] == 1 and a[-2] == 0:
            a.pop()
            a.pop()
            break
    return a[n % len(a)]
n=7
print((fib_fast(n+1))*(fib_fast(n) % 10))