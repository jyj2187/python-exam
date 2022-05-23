# 리스트에서 특정 값의 위치 찾기
# 순차 탐색 : 리스트의 처음부터 끝까지 원소를 하나씩 비교하면서 탐색한다.
import ex_list as ex


def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return -1


print(search_list(ex.v, 18))
print(search_list(ex.v, 33))
print(search_list(ex.v, 900))
