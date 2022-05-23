# 쉽게 설명한 선택 정렬
# 입력 리스트 a
# 출력 정렬된 새 리스트

# 주어진 리스트에서 최솟값의 위치를 돌려주는 함수
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def sel_sort(a):
    result = []  # 결과 리스트
    while a:  # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a)  # 최솟값의 위치를 저장
        value = a.pop(min_idx)  # 최솟값을 리스트에서 "빼내어(pop)" value에 저장
        result.append(value)  # 결과 리스트에 value를 저장
    return result


data = [2, 4, 5, 1, 3]
print(sel_sort(data))
