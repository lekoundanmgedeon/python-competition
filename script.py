
def fib_memo(n, memo={}):
    if n <= 0:
        return 1
    if n <= 1:  # error 1
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)  # error 2
    return memo[n]

for i in range(8):
    print(fib_memo(i), end=" ")
print()

