'''
< 문제 설명 >
사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다. 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다. 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고 ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고, "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.

그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning, 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.
'''

# 1차 풀이
'''
1차 시도 : 딕셔너리 활용. dictionary[name[i]] = yearning[i]
            key error 발생 (24번째 줄이 문제였으나 key error에 당황해서 if문 자체가 문제인줄 잘못 생각했음..)
'''            
def solution(name, yearning, photo):
    yearning_dict = {}
    answer = []
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
    # print(yearning_dict)
    
    for ph in photo:
        tmp = 0
        for j in ph:
            if yearning_dict[j] in yearning_dict:
                tmp += yearning_dict[j]
        answer.append(tmp)
    
    return answer
            
'''
2차 시도 : 딕셔너리에서 key error 발생시키지 않으려면 if문, try except, get 메서드 활용하는 방법 있는 것 확인함.
            if문과 try except문은 많이 써봤기에 get 메서드 활용함. (get 메서드 정리하자. 딕셔너리 사용시 자주 사용하게 될듯)
            그러나 여전히 key error 발생 (45번째 줄의 get 메서드 내부의 yarning_dict[j]가 문제였는데 엉뚱한 곳들만 수정했음)
'''
def solution(name, yearning, photo):
    yearning_dict = {}
    answer = []
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
    print(yearning_dict)
    
    
    for ph in photo:
        tmp = 0
        for j in ph:
            tmp += yearning_dict.get(yearning_dict[j], 0)
        answer.append(tmp)
        
    return answer

'''
3차 시도 : if문과 get 메서드 자체 문제는 없다고 생각하니 그 내부를 찬찬히 볼 여유가 생겨서 yearning_dict[j]를 이름 자체가 오도록 수정하여 해결함.
'''
def solution(name, yearning, photos):
    yearning_dict = {}
    answer = []
    for i in range(len(name)):
        yearning_dict[name[i]] = yearning[i]
    # print(yearning_dict)
    
    for photo in photos:
        tmp = 0
        for name in photo:
            tmp += yearning_dict.get(name, 0)
        answer.append(tmp)
        
    return answer


# 인상적인 다른 분의 풀이 설명
'''
간단한 문제인만큼 인덱스를 활용하여 1줄로 간략하게 쓴 코드가 인상적이었음.
회사에서 구간별 관절 각도를 체크할때 인덱스를 많이 활용했었는데 이 문제에서 떠올리지 못 한게 아쉬움.
'''
def solution(name, yearning, photos):
    answer = [sum([yearning[name.index(j)] for j in photo if j in name]) for photo in photos]
    return answer
