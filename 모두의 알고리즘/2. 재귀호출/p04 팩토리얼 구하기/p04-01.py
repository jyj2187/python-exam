#팩토리얼 알고리즘 1

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(fact(1))
print(fact(5))
print(fact(10))