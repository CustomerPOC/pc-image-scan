import json
import requests

def getAuthToken(url, username, password):
    loginURL = url + "/login"
    payload  = json.dumps({
        'username': username,
        'password': password
    })
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json; charset=UTF-8'
    }
    login    = requests.request("POST", loginURL, headers=headers, data=payload)
    response = login.json()
    token    = response["token"]
    
    return token