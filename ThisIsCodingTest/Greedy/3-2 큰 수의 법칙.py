# N 개의 자연수가 주어진다.
# M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 연속해서 K번을 초과하여 더할 수 없음.

# N, M, K를 공백으로 구분하여 입력 받는다.
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[N - 1]
second = data[N - 2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)
