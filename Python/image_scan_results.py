from functions import getAuthToken, get_size, convert_size
from datetime import datetime
import requests
import json
import os

url        = os.getenv("PRISMA_CLOUD_URL") #// Authenticate against Prisma Cloud API URL, i.e. (https://api2.prismacloud.io)
password   = os.getenv("PRISMA_CLOUD_SECRET")
username   = os.getenv("PRISMA_CLOUD_IDENTITY")
consoleURL = os.getenv("PRISMA_CLOUD_CONSOLE")
timestamp  = datetime.now().strftime('%Y%m%d_%H%M%S')
fileName   = f"scan_results_{timestamp}.json"
endpoint   = "api/v1/images"
method     = "GET"
body       = {}
apiURL     = f"{consoleURL}/{endpoint}"
params     = {
    "limit": 100,
    "offset": 0
}

headers = {
    'Accept': 'application/json',
    'x-redlock-auth': getAuthToken(url=url, password=password, username=username)
}

response      = requests.request(method, apiURL, headers=headers, data=body, params=params)
total_images  = response.headers.get('Total-Count')
response_data = response.json()

if total_images is None:
    print("No images found.")
    exit()

total_images = int(total_images)
print(f"Total image count: {total_images}")

all_results  = []  

while params["offset"] < total_images:
    print(f"Fetching records {params['offset']} to {params['offset'] + params['limit']}")
    
    response = requests.request(method, apiURL, headers=headers, data=body, params=params)
    current_data = response.json()
    
    all_results.extend(current_data)
    params["offset"] += params["limit"]

total_size = get_size(all_results)
print(f"Retrieved {len(all_results)} total records")
print(f"Data size: {convert_size(total_size)}")

with open(fileName, 'w') as f:
    json.dump(all_results, f, indent=4)