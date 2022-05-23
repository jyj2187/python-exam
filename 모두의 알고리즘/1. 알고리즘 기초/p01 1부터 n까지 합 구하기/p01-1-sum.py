# 1부터 n까지의 합을 출력하는 알고리즘 1
# 입력 정수 n
# 출력 1부터 n까지의 합

def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


print(sum_n(10))
print(sum_n(100))
