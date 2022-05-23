# 1부터 n까지의 합을 구하는 알고리즘 2

def sum_n(n):
    return n * (n + 1) // 2  # 슬래시 2개는 정수의 나눗셈


print(sum_n(10))
print(sum_n(100))
