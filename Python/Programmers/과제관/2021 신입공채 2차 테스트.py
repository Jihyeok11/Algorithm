import requests

x_auth_token = '7ef8fd29a5dc8bad9260e078a8f2c168'

base_url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
header = {
    x_auth_token : x_auth_token,
    'Content_type' : 'application/json',

}
data = {
    "problem": 1,
}

req = requests.post(base_url+"/start", headers= header, data= data)
print(req)