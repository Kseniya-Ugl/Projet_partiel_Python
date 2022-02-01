# c) Implémenter la suite de Fibonnaci

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        print()

data = list(fibonacci(10))
print(data)



