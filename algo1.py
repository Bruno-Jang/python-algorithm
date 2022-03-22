'''
함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한조건
n은 1이상 8000000000 이하인 자연수입니다.
'''

def solution(n):
    n_sorted = sorted(str(int(n)), reverse=True)
    answer = int(''.join(n_sorted))
    return answer

solution(873211)

'''
정렬하기 위해 str과 list 고민하다가 str이 더 간편할 것 같아서 str로 변환 후 정렬
정렬하면 작은 숫자가 먼저 정렬되서 reverse 사용
처음에는 for문을 살짝 고민했지만 너무 비효율적이어서 고민하다가 join 함수 사용
int로 반환 후 리턴

학습한 것
sort로 정렬하면 기본 형태는 list이다.

Q. 프로그래머스에서는 sorted(str(n), reverse=True) 이렇게 하면 테스트 도중 런타임 에러 발생
혹시나 해서 입력받는 n 값의 type도 찍어봤는데 int이던데 왜 다시 int로 감싸줘야 통과되는지 의문
'''
