# 일반적인 선택 정렬 알고리즘
# 내림차순

def sel_sort_desc(a):
    n = len(a)
    # temp = 0   #temp를 이용할 때
    for i in range(0, n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        # temp = a[i]
        # a[i] = a[min_idx]
        # a[min_idx] = temp #temp를 이용할 때 사용.
        a[i], a[max_idx] = a[max_idx], a[i]
        # print(a)    # 과정 출력


data = [2, 4, 5, 1, 3]
sel_sort_desc(data)
print(data)
