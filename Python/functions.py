import json
import requests
import sys

# Get authentication token
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

# Recursively calculate size of object and its contents in bytes
def get_size(obj, seen=None):

    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    
    if isinstance(obj, dict):
        size += sum(get_size(v, seen) for v in obj.values())
        size += sum(get_size(k, seen) for k in obj.keys())
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size(i, seen) for i in obj)
    
    return size

# Convert bytes to human readable format
def convert_size(size_bytes):
    """Convert size in bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0