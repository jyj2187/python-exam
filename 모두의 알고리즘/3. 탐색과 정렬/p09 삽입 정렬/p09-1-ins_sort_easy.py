# 쉽게 설명한 삽입 정렬

# 리스트 a에서 v가 들어갈 위치를 찾는 함수
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i  # v가 r[i]보다 작으면 그 위치를 돌려준다.
    return len(r)  # v보다 작은 원소가 없다면 맨 마지막 위치를 돌려준다.


def ins_sort(a):
    result = []
    while a:  # 리스트에 값이 있는 한 반복
        value = a.pop(0)  # 리스트에서 하나를 꺼낸다.
        ins_idx = find_ins_idx(result, value)  # 나온 값이 들어갈 자리를 찾는다.
        result.insert(ins_idx, value)  # 찾은 자리에 값 삽입 ( 그 뒤로는 한칸씩 밀려남 )
        # print(a, result)
    return result


data = [2, 4, 5, 1, 3]
print(ins_sort(data))
