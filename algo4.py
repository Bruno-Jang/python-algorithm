'''
부족한 금액 계산하기
< 문제 설명 >
새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.

< 제한사항 >
1. 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
2. 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
3. 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
'''

# 1차 시도
def solution(price, money, count):
    answer = 0
    for i in range(1, count + 1):
        answer += price * (i)
        
    if answer > money:
        return answer - money
    return 0

'''
많은 분들이 저처럼 이렇게 푸셨을거라고 생각한다...
문제 보고 바로 위의 방식이 떠올라서 풀었는데 아래의 풀이가 이 문제의 핵심을 꿰뚫은 느낌이다..!

def solution(price, money, count):
    return max(0, price * count * (count + 1) / 2 - money)

예시처럼 price = 3, count = 4, money = 20, result = 10
3 + 6 + 9 + 12 = 30
이걸 식으로 해보면
3 * (1 + 2 + 3 +4)
여기서 3은 price 이고 (1 + 2 + 3 +4) 는 횟수인 count 이다.
4 * (1/4 + 2/4 + 3/4 + 1)
여기서 4는 count 이기에
price * count * (1/4 + 2/4 + 3/4 + 1)
(1/4 + 2/4 + 3/4 + 1) = 2 + 1/2 = 5/2
이것도 수식으로 바꾸면 (count + 1) / 2 와 같으므로

price * count * (count + 1) / 2
'''