# 학생 번호로 학생 찾기
# 딕셔너리의 특성을 이용한다.

def get_name(s_no):
    s_info = eval(input(str(s_no) + "번 학생을 찾을 학생 목록을 입력해주세요."))
    if s_no in s_info:
        return s_info[s_no]
    else:
        return "잘모씀다?"


stu_info = {39: "Justin", 14: "John", 67: "Mike", 105: "Summer"}

print(get_name(14))
print(get_name(105))
print(get_name(50))

# in 연산자를 잊지 말자.
