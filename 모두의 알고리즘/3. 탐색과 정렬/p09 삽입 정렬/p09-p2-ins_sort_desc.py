# 삽입 정렬
# 내림차순

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]  # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j + 1] = key  # 찾은 삽입 위치에 key값을 저장
        # print(a)
        # 반복문 마지막에 j에서 1을 뺐으므로 j + 1 자리에 들어간다.


data = [2, 4, 5, 1, 3]
ins_sort(data)
print(data)
