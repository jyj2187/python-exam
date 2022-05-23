#짝짓기 알고리즘

def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print(a[i],'-',a[j])

name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pairs(name2)