#팩토리얼 알고리즘 2
#재귀호출 이용

def fact(n):
    if n <= 1:
        return 1
    return n * (fact(n-1))

print(fact(1))
print(fact(5))
print(fact(6))
print(fact(7))
print(fact(8))
print(fact(9))
print(fact(10))