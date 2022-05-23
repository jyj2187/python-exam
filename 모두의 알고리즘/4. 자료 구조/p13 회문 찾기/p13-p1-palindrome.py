# 주어진 문장이 회문인지 확인(문쟈열의 앞뒤를 서로 비교)
# 큐와 스택을 사용하지 않기

def palindrome(s):
    i = 0  # 문자열의 앞에서 비교할 위치
    j = len(s) - 1  # 문자열의 뒤에서 비교할 위치
    while i < j:  # 중간까지만 검사한다. (i가 j보다 같아지면 둘이 만나므로)
        # i 위치에 있는 문자가 알파벳이 아니라면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1
        # j 위치에 있는 문자가 알파벳이 아니라면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1
        # i 위치와 j위치의 문자를 비교하고 다르면 회문이 아님을 출력
        elif s[i].lower() != s[j].lower():
            return False
        # i와 j 위치의 문자가 서로 같으면 다음 비교 대상으로 넘어감
        else:
            i += 1
            j -= 1

    return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))
