#문제 접근 : 문제를 보고 정렬만 잘하면 수월하게 풀 수 있을거라 생각하였다.

def solution(genres, plays):
    song = {}
    answer = []
    for i in range(len(genres)):    #우선 장르들을 갯수를 파악하기 위해서 딕셔너리로 정의해준다
        if genres[i] in song:
            song[genres[i]] += plays[i]
        else:
            song[genres[i]] = plays[i]
    song = sorted(song.items(), key = lambda x:x[1],reverse=True)   #노래가 많은 순으로 딕셔너리 정렬
    for i in range(len(song)):  #장르의 갯수만큼 반복문 돌기
        cnt = []
        for j in range(len(genres)):    #입력받은 노래를 돌면서
            if genres[j] == song[i][0]: #같은 장르가 있으면 
                cnt.append([plays[j],j])    #임시 배열에 추가
        cnt = sorted(cnt, key = lambda x:x[0],reverse=True) #임시 배열에서도 노래 갯수 큰 순서대로 정렬, 3번째 조건은 처음 들어갈때부터 지켜짐
        for k in range(len(cnt)):   #2개만 추가
            if k == 2:
                break
            else:
                answer.append(cnt[k][1])
    return answer