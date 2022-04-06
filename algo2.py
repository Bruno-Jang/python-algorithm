'''
< 없는 숫자 더하기 >
* 문제 설명
0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

* 제한 사항
1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 원소 ≤ 9
numbers의 모든 원소는 서로 다릅니다.
'''

# 1차 풀이 문제를 보고 for 문을 통해서 remove 메서드를 써야겠다고 생각했다.
def solution(numbers):
    num_list = [1,2,3,4,5,6,7,8,9,0]
    
    for n in numbers:
        num_list.remove(n)
        
    print(sum(num_list))
    return sum(num_list)

solution([1,2,3,4,6,7,8])

# 다른 분의 정답을 봤는데 정말 획기적이다.. 라는 생각밖에 안 들었다.
'''
def solution(numbers):
    return 45 - sum(numbers)
'''