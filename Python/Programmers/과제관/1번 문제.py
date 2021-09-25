import requests, json, heapq, random

def score(base_url, header):
    # 효율성 점수, 정확성 점수1, 정확성 점수2, 총점
    req = requests.get(base_url + "/score", headers = header).json()
    print(req)

# id(매칭 기다리는 유저 ID), from(매칭을 대기한 시간)
def waiting_user(base_url, header):
    req = requests.get(base_url + "/waiting_line", headers=header).json()
    return req['waiting_line']

# win (이긴유저 ID), lose(진 유저 ID), taken(걸린 시간)
def game_result(base_url, header):
    req = requests.get(base_url + "/game_result", headers=header).json()
    return req['game_result']

# id, grade
def user_info(base_url, header):
    req = requests.get(base_url + "/user_info", headers=header).json()
    print(req)

# status(ready), time(현재시간)
def game_match(base_url, header, li):
    data = {
        "pairs" : li
    }
    req = requests.put(base_url + "/match", headers = header, data=json.dumps(data)).json()
    print(req)

# id랑 grade값이 있는 것을 전달해줘야한다.
def change_grade(base_url, header, ba):
    data = {
        "commands" : ba,
    }
    print(ba)
    req = requests.put(base_url + "/change_grade", headers = header, data= json.dumps(data)).json()
    print(req)

def startproblem(base_url, token, problem):
    user_count = [0, 30, 900]
    header_start = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json',
    }
    data = {
        "problem" : problem,
    }
    # auth_key, problem, time
    req = requests.post(base_url + "/start", headers=header_start, data=json.dumps(data)).json()
    auth_key = req['auth_key']
    header = {
        'Authorization': auth_key,
        'Content-Type': 'application/json',
    }
    # 유저 수 만큼 users 생성
    users = []
    for i in range(user_count[problem] + 1):
        users.append([i+1, 40000])


    wait_user = []
    for _ in range(596):
        # 이 시간에 싸울 사람
        game_match(base_url, header, wait_user)
        # {'id': 17, 'from': 1}
        wait_user = []
        lobby = []
        for res in waiting_user(base_url, header):
            heapq.heappush(lobby, [users[res['id']][1], res['id']])
        
        matching = []
        while lobby:
            a = heapq.heappop(lobby)
            matching.append(a[1])
            if len(matching) == 2:
                if users[matching[0]][1] - users[matching[1]][1] <= 20000:
                    wait_user.append(matching)
                else:
                    heapq.heappush(lobby, a)
                matching = []
                

        if game_result(base_url, header):
            for i in game_result(base_url, header):
                e = random.randint(-5, 5)
                m, wid, lid = i['taken'], i['win'], i['lose']
                r = min(int((40 + e- m) * 99000 / 35) + users[lid][1], 20000)
                r = max(r, users[lid][1])
                users[wid][1] = min(r // 2, 100000)
                users[lid][1] -= 10
    ba = []

    #{ "id": 1, "grade": 1900 }
    for i in range(user_count[problem]):
        grade = users[i][1] // 10
        ba.append({"id": users[i][0], "grade" : grade})

    change_grade(base_url, header, ba)
    score(base_url, header)


base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
x_auth_token = '344b4e0dd5f4660f0303f4bb3552239d'
startproblem(base_url, x_auth_token, 1)