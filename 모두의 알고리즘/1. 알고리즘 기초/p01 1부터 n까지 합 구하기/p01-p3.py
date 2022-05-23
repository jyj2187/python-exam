# 1부터 n까지의 제곱의 합을 구하는 알고리즘 2
# O(1)

def square_sum(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(square_sum(10))
