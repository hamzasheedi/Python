def fibonacci(n):
    a, b = 0, 1  # Pehle do numbers define karna
    for _ in range(n):
        print(a, end=" ")  # Current number print karo
        a, b = b, a + b  # Next number calculate karo

# Example: Print first 10 Fibonacci numbers
fibonacci(10)
