#피보나치 수열 번호 구하기
#0과 1부터 순차적으로 더해간다.
#재귀호출 탈출 조건은 0과 1.

def fibo(n):
    if n <= 1:
        return n #n이 1보다 작으면 0 또는 1.
    return fibo(n-2) + fibo(n-1)

print(fibo(7))
print(fibo(10))
