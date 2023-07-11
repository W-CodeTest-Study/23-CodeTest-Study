def solution(n, times):
    # times배열에 숫자분배, n을 숫자분배해서 가장 작은 값 구하기
    # 현재 케이스는 4,2로 분배한 상태에서 가장 큰 값이 answer후보 중 가장 작은 값이 answer
    # answer//10=2=20, answer//7=4=28 이 중 큰거 28
    # n을 분배하는 기준을 모르겠당...ㅎㅎ -> 노가다로

    times.sort()
    count_table = [0 for i in range(len(times))]
    temp_table = [0 for i in range(len(times))]  # 임시 count테이블

    candidate = [0 for i in range(len(times))]  # 임시테이블을 통해 구한 최대시간을 넣음
    arr = []
    # n이 1일때부터 최선의 방법으로 올라가기
    for num in range(1, n+1):

        # 그냥 심사국 i번째부터 일일이 다 들어가서 그거의 최선선택
        for i in range(len(times)):
            # 임시테이블은 이전 채택된 테이블로 최신화
            for k in range(len(times)):
                temp_table[k] = count_table[k]

            temp_table[i] += 1  # 순서대로 1씩넣기

            # 각 들어갔을때 걸리는 시간 구하고 후보테이블에 저장
            arr = []
            for j in range(len(times)):
                arr.append(temp_table[j]*times[j])
            candidate[i] = max(arr)

        # 최대시간중 최소값인 index찾아서 그걸로 채택
        count_table[candidate.index(min(candidate))] += 1

    answers = []
    for i in range(len(times)):
        answers.append(count_table[i]*times[i])

    answer = max(answers)

    return answer
