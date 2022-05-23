#1부터 n까지의 합 구하기 알고리즘 3
#재귀호출 이용

def sum_n(n):
    if n == 0:
        return 0
    return n + (sum_n(n-1))

print(sum_n(5))
print(sum_n(10))
print(sum_n(100))