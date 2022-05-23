# 두 번 이상 나온 이름 찾기
# 딕셔너리의 특성을 이용한다.

def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result


name_list = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name_list))

name_list2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name_list2))
