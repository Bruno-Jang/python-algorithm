'''
< 전화번호 목록 >
< 문제 설명 >
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

* 구조대 : 119
* 박준영 97 674 223
* 지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

< 제한사항 >
1. phone_book의 길이는 1 이상 1,000,000 이하입니다.
2. 각 전화번호의 길이는 1 이상 20 이하입니다.
3. 같은 전화번호가 중복해서 들어있지 않습니다.
'''
# 1차 풀이
# def solution(phone_book):
#     tmp = {i: len(phone_book[i]) for i in range(len(phone_book))}
#     short = min(tmp, key=tmp.get)
#     print(short)
    
#     min_value = phone_book[short]
#     print(min_value)
#     cnt = 0
#     for i in phone_book:
#         if i.startswith(min_value):
#             cnt += 1
#         if cnt >= 2:
#             print(False)
#             return False
#     print(True)
#     return True

# phone_book = ["12","123","1235","567","88"]
# solution(phone_book)
'''
1차 풀이 로직
1. 전달받은 리스트의 길이를 딕셔너리로 전환 (key는 리스트의 인덱싱, value는 길이)
2. 문자열의 길이가 가장 짧은 것을 찾기
3. startswith 메서드 사용하여 길이가 가장 짧은 문자열로 시작하는지 체크 - 있으면 cnt += 1
4. for문이라 해당 문자열도 체크하기에 cnt 값이 2가 되면 False 리턴 아니라면 마지막에 True 리턴

그런데 총 20개의 정확성 테스트 중 3개 실패, 4개의 효율성 테스트 중 1개 실패
정확성은 가장 짧은 문자열이 2개 이상일 경우 1개만 고르기에 나머지는 테스트하지 못 하는 문제인듯
'''

# 2차 풀이 (해시 문제에 적합한 방법)
# def solution(phone_book):
#     answer = True
#     tmp = {}
#     for phone_number in phone_book:
#         tmp[phone_number] = 1           # 전달 받은 리스트를 딕셔너리로 전환

#     for phone_number in phone_book:
#         num_str = ''
#         for num in phone_number:        # 정렬을 하지 않기에 상대적으로 긴 문자열의 경우 앞에서부터 인덱싱 하듯이 추출한 데이터를 phone_book 리스트에서 같은게 있다면 False 리턴
#             num_str += num
#             if num_str in tmp and num_str != phone_number:
#                 print(False)
#                 return False
#     return answer

# solution(["12","456", "135", "123"])


# 3자 풀이
phone_book = ["12","456", "135", "123"]
def solution(phone_book):
    answer = True
    tmp = {}
    for phone_number in phone_book:
        tmp[phone_number] = 1
        
    print(tmp)
        
    min_len = min(len(i) for i in phone_book)
    print(min_len)
    
    for phone_number in phone_book:
        print(type(phone_number[:min_len]), phone_number[:min_len])
        if tmp.get(phone_number[:min_len]) and phone_number[:min_len] != phone_number:
            print(False)
            return False
    print(answer)
    return answer
    
solution(phone_book)  
    
'''
2차 풀이 방식을 보다 효율적인 방식으로 해보고자 했습니다.
문자열 길이가 가장 적은 것을 찾아서 비교할 때 그 길이만큼 인덱싱 한 것을 뽑아내서 비교해보는 것입니다.
그러나 채점 결과 91.7점으로 정확성 테스트 15, 19번에서 실패하네요
그럼에도 불구하고 유의미한 도전이었다고 생각합니다!
'''