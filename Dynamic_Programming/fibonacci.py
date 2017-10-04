n = int(input("Enter n: "))

fibonacci_numbers = [0, 1, 1]
fibonacci_numbers.extend([-1]*(n-2))

def fibonacci(n, fib=fibonacci_numbers):
    if n < 3:
        return 1
    elif fib[n] > 0:
        return fib[n]
    else:
        fib[n] = fibonacci(n-1, fib) + fibonacci(n-2, fib)
        return fib[n]

print fibonacci(n, fibonacci_numbers)