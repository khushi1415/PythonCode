def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def demo():
    return

result = factorial(5)
print(f"The factorial of 5 is {result}")
