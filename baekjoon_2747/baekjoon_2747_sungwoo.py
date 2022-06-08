def fib(n):
    a = 0
    b = 1
    if n == 1 or n == 2:
        print(1)
    else:
        while n >= 1:
            a, b = b, a + b
            n = n - 1
        print(a)
c = int(input())
fib(c)