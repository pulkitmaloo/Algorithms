n = int(input("Enter n: "))

# Top down - better for multiple queries
fibonacci_numbers = [0, 1, 1]
def top_down_fibonacci(n, fib=fibonacci_numbers):
    if n < 3:
        return fib[n]
    elif len(fib)-1 >= n:
        return fib[n]
    else:
        fib.append(top_down_fibonacci(n-1, fib) + top_down_fibonacci(n-2, fib))
        return fib[n]

# Bottom up - saves space and avoids stack overflow problem
# Could be modified to save the numbers in an array as well
def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(n-1):
            c = a + b
            a = b
            b = c
        return b

print fibonacci(n)