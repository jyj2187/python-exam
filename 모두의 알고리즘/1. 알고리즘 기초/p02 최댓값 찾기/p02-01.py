#최댓값을 찾는 알고리즘 1

def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1,n):
        if a[i] > max_v:
            max_v = a[i]
    return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))
