# 주어진 동전 n개 중에 가짜 동전을 찾아내는 알고리즘
# 입력: 전체 동전 위치의 시작과 끝
# 출력: 가짜 동전의 위치 번호

# 무게 재기 함수
def weigh(a, b, c, d):
    fake = 29
    # fake가 a와 b 사이에 있으면 -1
    if a <= fake and fake <= b:
        return -1
    # fake가 c와 d 사이에 있으면 1
    if c <= fake and fake <= d:
        return 1
    # fake가 해당 위치에 없으면 0
    return 0


def find_fakecoin(left, right):
    # 종료 조건 : 가짜 동전이 있을 범위 안에 동전이 한개 뿐이면 그 동전이 가짜 동전
    if left == right:
        return left
    # 동전을 두 그룹으로 나눔
    # 동전 수가 홀수면 두 그룹으로 나누고 한개가 남음
    # 고로 1을 더해서 나머지 없이 나눈다
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1
    # 나눠진 두 그룹을 weigh함수를 이용하여 저울질
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    # 그룹 1에 대한 재귀
    if result == -1:
        return find_fakecoin(g1_left, g1_right)
    # 그룹 2에 대한 재귀
    elif result == 1:
        return find_fakecoin(g2_left, g2_right)
    # 두 그룹의 무게가 같으면
    # 두 그룹으로 나뉘지 않고 남은 나머지 한 개의 동전이 가짜 동전 = right(맨 마지막 동전)
    else:
        return right


n = 100
print(find_fakecoin(0, n - 1))