# 리스트에서 특정 값의 모든 위치를 리스트로 돌려주는 알고리즘
import ex_list as ex


def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if x == a[i]:
            result.append(i)
    return result


v = [17, 92, 18, 33, 58, 5, 33, 42, 18]
print(search_list(ex.v, 18))
print(search_list(v, 18))
print(search_list(ex.v, 900))
