# 시간 복잡도를 줄이는 방법
# 반복되는 수열에 대해서 파악
# 항상 큰 수를 K번씩 더하고 작은 수를 한번 씩 더한다.
# => K+1의 형식을 M이 될때까지 반복함
# 즉 (M / (K+1)) * K + M % (K+1)은 큰 수를 더하는 횟수가 됨
# M - (M / (K+1)) * K + M % (K+1)는 두 번째로 큰 수를 더하는 횟수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)
