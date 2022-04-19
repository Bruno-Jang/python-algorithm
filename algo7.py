'''
베스트앨범
< 문제 설명 >
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

< 제한 사항 >
1. genres[i]는 고유번호가 i인 노래의 장르입니다.
2. plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
3. genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
4. 장르 종류는 100개 미만입니다.
5. 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
6. 모든 장르는 재생된 횟수가 다릅니다.
'''

# 1차 풀이
def solution(genres, plays):
    total = {}
    result = []
    
    for g, p in zip(genres, plays):
        if g in total:
            total[g] += p
        else:
            total[g] = p
    
    tmp = {g: {idx: plays[idx] for idx in range(len(genres)) if g == genres[idx]} for g in genres}    
    
    while total:
        max_k = max(total, key=total.get)
        
        for i in range(len(tmp[max_k])):    
            if len(tmp[max_k]) > 2:
                result.append(max(tmp[max_k], key=tmp[max_k].get))
                del tmp[max_k][max(tmp[max_k], key=tmp[max_k].get)]
                result.append(max(tmp[max_k], key=tmp[max_k].get))
                del tmp[max_k][max(tmp[max_k], key=tmp[max_k].get)]
                break
            
            elif len(tmp[max_k]) > 0:
                result.append(max(tmp[max_k], key=tmp[max_k].get))
                del tmp[max_k][max(tmp[max_k], key=tmp[max_k].get)]
        del total[max_k]

    return result

'''
대략 90%정도 생각했던대로 코드를 구현했고 정답은 다 맞았지만
부족한 부분과 어떤 로직으로 작성하려고 했는지 적어보려고 합니다.

< 로직 >
1. total = 장르끼리 총 합 체크
2. tmp = 장르별 {인덱스: 값 ...}
3. total에서 값이 더 큰 것의 키를 max_k라는 변수에 담는다. ex) 'pop'
4. 해당 장르의 딕셔너리 길이를 체크하여 2개 초과인지 아닌지 체크
4. 2개 초과 : max value에 해당하는 key를 result에 넣고 해당 key를 제거 (2번 반복)
5. 2개 이하 : max value에 해당하는 key를 result에 넣고 해당 key를 제거
6. 4번 또는 5번을 하면 해당 key를 tmp에서 제거한다.
7. 인덱스를 담은 result를 리턴한다.

< 해결해야 할 점 >
1. 해당 장르의 딕셔너리 길이가 2개 초과일 때 2번 반복하는 코드를 하드코딩한 점
2. 해당 장르의 딕셔너리 길이가 2개 초과일 때 break를 하는게 테스트 케이스에 따라 안 될 수도 있다고 생각한다.
'''

# 다른 분의 정말 깔끔한 코드 - 블로그에 정리
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play
