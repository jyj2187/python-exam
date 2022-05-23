# 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이 때 N은 행의 개수, M은 열의 개수를 의미한다.
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 즉, 모든 행의 가장 낮은 수의 카드를 뽑아 가장 높은 숫자를 뽑은 사람이 이기는 게임.
# 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# N과 M이 주어지고
# 두번째 줄부터 N * M 형태의 행렬이 주어진다.

# min() 함수를 이용하는 방식
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)
