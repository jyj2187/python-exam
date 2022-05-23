# 1부터 n까지의 제곱의 합을 구하는 알고리즘 1
# O(n)

def square_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += (i * i)
    return s


print(square_sum(10))
