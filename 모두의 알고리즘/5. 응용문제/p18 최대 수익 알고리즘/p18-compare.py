import time
import random


# 최대 수익 느린 알고리즘 O(n^2)
def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


# 최대 수익 빠른 알고리즘 O(n)
def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


def test(n):
    # 테스트 케이스 생성 (5000부터 20000까지의 난수를 주가로 사용)
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))

    # 느린 알고리즘 테스트 O(n^2)
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # 빠른 알고리즘 테스트 O(n)
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    # 결과 출력 : 테스트 케이수 개수, 느린 알고리즘 속도, 빠른 알고리즘 속도
    print(n, mps, mpf)

    # 결과 출력에 걸리는 시간 비교
    m = 0
    if time_fast > 0:  # 컴퓨터 환경에 다라 빠른 알고리즘 시간이 0으로 측정될 수 있음
        # 이 경우에는 0을 출력
        m = time_slow / time_fast  # 느린 알고리즘 시간 / 빠른 알고리즘 시간
    # 느린 알고리즘 수행 시간, 빠른 알고리즘 수행 시간, 계산 시간 차이
    print("%.10f %.10f %.5f" % (time_slow, time_fast, m))


test(100)
test(10000)
test(100000)  # 수행 시간이 오래 걸림
