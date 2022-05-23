# n의 범위가 크다면?
# n이 k의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 작성한다.

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)

    n = target
    if n < k:
        break
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)