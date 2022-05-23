# 주어진 동전 n개 중에 가짜 동전(fake)를 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝(0, n-1)
# 출력: 가짜 동전의 위치 번호

# 무게 재기 함수
# a에서 b까지에 놓인 동전과 c에서 d까지에 놓인 동전의 문제를 비교
# a ~ b에 가짜 동전이 있으면 (가벼우면) : -1
# c ~ d에 가짜 동전이 있으면 (가벼우면) : 1
# 가짜 동전이 없으면(양쪽 무게가 같으면) : 0
def weigh(a, b, c, d):
    fake = 29
    if a <= fake and fake <= b:
        return -1
    if c <= fake and fake <= d:
        return 1
    return 0


def find_fakecoin(left, right):
    for i in range(left + 1, right + 1):
       result = weigh(left, left, i, i)
       if result == -1:
           return left
       elif result == 1:
           return i

    return -1

n = 100
print(find_fakecoin(0,n-1))