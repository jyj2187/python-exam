#리스트의 학생 번호를 찾으면 해당 번호의 학생 이름을 출력하는 프로그램

def search_stu(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(0,n):
        if find_no == s_no[i]:
            return s_name[i]
    return "?"

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(search_stu(stu_no, stu_name, 39))
print(search_stu(stu_no, stu_name, 14))
print(search_stu(stu_no, stu_name, 1))