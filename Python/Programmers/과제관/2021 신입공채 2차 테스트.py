import requests, json
from requests.api import head
def f_start(x_auth_token, base_url, problem):
    header = {
        'X-Auth-Token' : x_auth_token,
        'Content-Type' : 'application/json',
    }
    data = {
        "problem" : problem,
    }
    req = requests.post(base_url+"/start", headers= header, data= json.dumps(data))
    auth_key = req.json()['auth_key']
    header = {
        'Authorization' : auth_key,
        'Content-Type' : 'application/jons',
    }
    f_simulate(base_url, header)
    for i in f_locations(base_url, header):
        print(i)
    for i in f_trucks(base_url, header):
        print(i)
    f_score(base_url, header)

def f_trucks(base_url, header):
    req = requests.get(base_url + "/trucks", headers=header).json()['trucks']
    return req

def f_locations(base_url, header):
    req = requests.get(base_url + "/locations", headers=header).json()['locations']
    return req

def f_simulate(base_url, header):
    data = {
        'commands' : [
            { "truck_id": 0, "command": [2, 5, 4, 1, 6] }
        ]
    }
    requests.put(base_url + "/simulate", headers = header, data=json.dumps(data))

def f_score(base_url, header):
    print(requests.get(base_url + "/score", headers=header).json()['score'])
    
x_auth_token = 'd738a1f3147ffa15390c333f1faf7b62'
base_url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
f_start(x_auth_token, base_url, 1)
# f_start(x_auth_token, base_url, 2)