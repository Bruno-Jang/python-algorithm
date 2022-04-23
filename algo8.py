'''
가장 큰 수
< 문제 설명 >
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

< 제한 사항 >
1. numbers의 길이는 1 이상 100,000 이하입니다.
2. numbers의 원소는 0 이상 1,000 이하입니다.
3. 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''

# 1차 풀이
'''
sort와 lambda를 활용하여 정렬하여 풀 생각이었는데 3, 30, 34처럼 앞자리(1자릿 수도 포함)가 같은 경우의 비교 할 방법을 못 찾았다.
lambda도 if문 사용이 가능하던데 이 경우에는 쓰기에는 어려운듯하다.
'''
def solution(numbers):
    answer = ''
    
    tmp = sorted(numbers, key=lambda x : (str(x)[0], str(x)[1]) if str(x)[1] != None else str(x)[0], reverse=True)

    for i in tmp:
        answer += str(i)
    return answer

# 2차 풀이 (lambda와 if문만을 사용해서 풀고 싶었는데 이 방법밖에 없는 것 같다..)
def solution(numbers):
    answer = ''
    
    if set(numbers) == {0}:
        return '0'
    
    res = sorted(numbers, key=lambda x : str(x) * 3, reverse=True)
    
    for i in res:
        answer += str(i)
    return answer
'''
1. 리스트에 값이 모두 0인 경우 문자 '0' 리턴
2. numbers의 원소가 1000 이하라고 하니 한 자릿수인 수를 3자릿수에 맞춰서 비교
'''