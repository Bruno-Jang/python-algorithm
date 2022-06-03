'''
기능개발
< 문제 설명 >
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

< 제한 사항 >
* 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
* 작업 진도는 100 미만의 자연수입니다.
* 작업 속도는 100 이하의 자연수입니다.
* 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.
'''

# 1차 풀이
'''
1차 시도 : While과 Queue를 활용하되 for문은 사용하지 않고 풀어보려고 했으나 실패 (while과 for문을 함께 쓰면 성능상 많이 떨어지지 않을까 하는 막연한 걱정으로 인해..)

2차 시도 : 
1. 각 작업이 완료되는 기간을 계산해서 days라는 리스트에 추가
2. days 리스트의 인덱싱을 활용하여 0번째 값 기준으로 다음 인덱싱 값과 비교하여 이하의 값일 경우 cnt += 1 수행 / 아니면 적립된 cnt 값을 answer에 append 하는 것이 기본 로직

하루 넘게 고민해봤으나 코드 구현이 안 되서 추후에 다시 작성해봐야 할 듯 합니다.
'''
def solution(progresses, speeds):
    # days는 각 작업이 완료되는 시점을 계산한 것
    days = []
    answer = []
    
    # 각 작업이 완료되는 시간을 계산하는 로직
    for i in range(len(progresses)):
        count = 0
    
        progress = 100 - progresses[i]
        if progress % speeds[i] == 0:
            count = progress // speeds[i]
        
        else:
            count = (progress // speeds[i]) + 1
        days.append(count)

    # days[0]을 pop하기 전에 변수에 저장
    tmp = days[0]
    
    cnt = 0
    i = 0
    while days:
        tmp = days[0]
        
        if days[i] <= tmp:
            cnt += 1
            i += 1
        
        elif tmp == days[-1]:
            cnt += 1
            answer.append(cnt)
            days.clear()
        
        else:
            answer.append(cnt)
            cnt = 0
            i = 0
            del days[:i]
                
    print(answer)
    return answer



# 인상적인 다른 분의 풀이 설명
'''
1. progresses 리스트의 가장 첫번째 값이 몇 번만에 100 이상이 되는지 체크하여 그 다음의 값에 해당 횟수 * 해당 speeds 값을 곱하여 100 이상이 되는지 체크
2. 100 이상이 되면 해당 인덱스 pop하여 제거하고 아니라면 count 값의 유무에 따라 answer에 append 또는 time += 1 진행
3. 마지막 값이 100 이상이 되어 count 값에 추가하면 94번째 줄의 로직 실행하여 answer 값 리턴

이 문제의 키 포인트를 잘 파악한 것 같습니다. 첫 번째 값이 100 이상이 되어야 의미가 있으므로 첫 번째 값이 언제 100 이상이 되는지부터 체크하는 것이 인상적이었고
그 횟수를 기준으로 다음 값 체크하는 것 또한 인상적이었습니다.
'''
def solution(progresses, speeds):
    answer = []
    
    time = 0
    count = 0
    while progresses:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0

            time += 1

    answer.append(count)
    return answer
