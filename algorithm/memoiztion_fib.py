def fib_memo(n, cache):
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]

def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)

print(fib(10))
print(fib(50))
print(fib(100))