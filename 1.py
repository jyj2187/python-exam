h, m = map(int, input().split())
need = eval(input())

if need >= 60:
    h += 1
    need -= 60

cook = m + need

if cook >= 60:
    h += 1
    m = cook - 60
    if h >= 24:
        h -= 24
else:
    m = cook
print("%d %d" % (h, m))
