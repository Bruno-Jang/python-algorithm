'''
K번째수

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

< 제한 사항 >
* array의 길이는 1 이상 100 이하입니다.
* array의 각 원소는 1 이상 100 이하입니다.
* commands의 길이는 1 이상 50 이하입니다.
* commands의 각 원소는 길이가 3입니다.
'''


# 1차 풀이
'''
1. 2차원 리스트인 commands를 for loop을 통해 분해
2. 1번 작업을 통해 각 리스트에는 3개의 값이 담겨 있으므로 3개의 변수에 할당
3. 인덱싱을 활용하여 잘라내고 그 후 정렬
4. 2번 작업의 마지막 값(순서)에 해당하는 값을 answer라는 리스트에 append하여 for loop 끝나면 리턴
'''
def solution(array, commands):
    answer = []
    
    for c_list in commands:
        i, j, k = c_list
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    return answer


# 2차 풀이
'''
위의 1차 풀이를 list comprehension을 활용하여 좀 더 간단하게 정리
1줄에 작성한 것은 좋지만 변수들이 많이 들어가서 직관성은 조금 떨어지는 것 같은 단점이 있다.
'''
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]


# 다른 분들의 풀이 (map & lambda 함수 활용)
'''
알고리즘 문제 풀다 보면 아래처럼 map 함수와 lambda 함수를 자유자재로 활용하시는 분들이 많으시던데
이번 기회에 배울 수 있어서 좋았고 앞으로 다른 문제에 저도 활용해보고자 합니다.
로직 자체는 같습니다.
2차원 리스트를 1차원 리스트로 가져왔을 때 무조건 변수는 3개여야 한다고 생각하고 로직을 짰었는데
이렇게 map 함수와 lambda 함수를 활용해서 효율적으로 짤 수 있다는 것이 놀랍습니다.
'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
