'''
달리기 경주
문제 설명
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
'''

# 1차 시도 (일부 테스트들(9~13) 시간 초과)
def solution(players, callings):
    answer = []
    answer = players
    for call_player in callings:
        player_called_idx = players.index(call_player)
        
        answer[player_called_idx - 1], answer[player_called_idx] = answer[player_called_idx], answer[player_called_idx - 1]
    
    return answer

# 2차 시도
'''
예를 들어 callings에서 kai 등 각 선수가 총 몇번 불렸는지를 체크해서 딕셔너리에 담고 여기에서 가장 적은 수를 모두 빼주고 남은 사람에 대한 숫자만큼 players에서 순서 변경해주면 되지 않을까?
=> 엎치락 뒤치락 하는 경우 등을 고려해봤을 때 이 방법은 맞지 않음
'''
def solution(players, callings):
    answer = []
    answer = players
    for call_player in callings:
        player_called_idx = players.index(call_player)
        
        answer[player_called_idx - 1], answer[player_called_idx] = answer[player_called_idx], answer[player_called_idx - 1]
    
    return answer

# 3차 시도
'''
리스트에서 값을 찾으려면 데이터가 커지는 것에 비례하여 속도가 느려지고 전체를 탐색해야 하지만
딕셔너리의 경우 해쉬 테이블을 통해 key를 활용하여 value를 가져오기 때문에 데이터 양이 많아져도 속도 차이가 거의 없다고 함.
'''
def solution(players, callings):
    answer = []
    players_dict = {player: idx for idx, player in enumerate(players)}
    # print(players_dict)
    
    for call in callings:
        current_rank = players_dict[call]
        
        players_dict[call] -= 1
        players_dict[players[current_rank - 1]] += 1
        
        players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
    
    return players

'''
다른 분의 인상적인 풀이를 참고하여 다시 작성해본 코드 (lambda sorting)
최대한 적은 변수(또는 코드를 적게 작성)를 활용하는 등 짧게 코드 작성하는 것만이 좋은 것인줄 알았는데
dict처럼 기능에 따라 2개의 변수에 용도에 맞게 값들을 각각 저장하여 활용하는 것이 좋을때도 있겠구나라는 생각을 했음.
간단하여 함수를 만들 필요가 없을 경우 lambda 활용을 더 많이 해보고자 함.
'''
def solution(players, callings):
    ranks_dict = {index: value for index, value in enumerate(players)}
    players_dict = {value: index for index, value in enumerate(players)}
    
    for call in callings:
        rank = players_dict[call]
        before_player = ranks_dict[rank - 1]
        
        ranks_dict[rank - 1], ranks_dict[rank] = ranks_dict[rank], ranks_dict[rank - 1]
        players_dict[before_player], players_dict[call] = players_dict[call], players_dict[before_player]
        
    sorted_players = dict(sorted(players_dict.items(), key=lambda x: x[1]))
        
    return list(sorted_players.keys())
