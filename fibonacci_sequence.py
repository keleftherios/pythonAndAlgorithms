def fibonacci(n):
    if n < 2:
        return str(n)
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(str(a))
        a, b = b, a + b
    return ' '.join(result)

def fibonacci_v2(n):
    if n <= 1:
        return n
    else:
        return fibonacci_v2(n-2) + fibonacci_v2(n-1)

if __name__ == "__main__":
    S = fibonacci(10)
    print(S)

    for num in range(10):
        print(fibonacci_v2(num), end = ' ')
    print()