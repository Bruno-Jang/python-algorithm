'''
< 완주하지 못한 선수 >
< 문제 설명 >
수많은 마라톤 선수들이 마라톤에 참여하였습니다.
단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

< 제한사항 >
1. 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
2. completion의 길이는 participant의 길이보다 1 작습니다.
3. 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
4. 참가자 중에는 동명이인이 있을 수 있습니다.
'''
# 1차 풀이
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    
    answer = participant[0]
    return answer

'''
for문을 사용해서 정확성 테스트는 통과했으나 효율성 테스트에 실패했다.
그래서 해시 문제이기에 딕셔너리를 활용하여 해결하고자 리스트의 요소를 딕셔너리의 키와 값으로 변형시키면 어떨까라는 생각에 시도해봤습니다. (요소 == 키 == 값)
completion_dict = {name: name for name in completion}
출력 예시 : {'eden': 'eden', 'kiki': 'kiki'}
동명이인 부분이 해결되지 않아서 다른 방법을 찾아봤습니다.
'''

# 2차 풀이
def solution(participant, completion):
    tmp = {}
    for name in participant:
        if name in tmp:
            tmp[name] += 1
        else:
            tmp[name] = 1
            
    for name in completion:
        if tmp[name] == 1:
            del tmp[name]
        else:
            tmp[name] -= 1
    
    answer = list(tmp.keys())[0]
    return answer

'''
다른 분의 블로그를 참고해서 풀었는데 딕셔너리에 대해 잘 알고 있었다면
보다 쉽게 풀 수 있었을 것 같습니다.
'''

# 3차 풀이
from collections import Counter

def solution(participant, completion):
    tmp = Counter(participant) - Counter(completion)
    answer = list(tmp.keys())[0]
    return answer

'''
Counter 활용하여 굉장히 간단하게 풀 수 있었습니다.
'''
