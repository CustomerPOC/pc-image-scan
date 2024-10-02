from login import getAuthToken
import requests
import json
import os;

url        = os.getenv("PRISMA_CLOUD_URL") #// Authenticate against Prisma Cloud API URL, i.e. (https://api2.prismacloud.io)
password   = os.getenv("PRISMA_CLOUD_SECRET")
username   = os.getenv("PRISMA_CLOUD_IDENTITY")
consoleURL = os.getenv("PRISMA_CLOUD_CONSOLE")

endpoint   = "api/v1/images"
method     = "GET"
body       = {}
apiURL     = f"{consoleURL}/{endpoint}"
params     = {
    "limit": 1,
    "offset": 0
}

token   = getAuthToken(url=url, password=password, username=username)
headers = {
    'Accept': 'application/json',
    'x-redlock-auth': token
}

response     = requests.request(method, apiURL, headers=headers, data=body, params=params)
total_images = response.headers.get('Total-Count')
data         = response.json()

if (total_images <= params["limit"]):
    print(data)

if (total_images <= params["limit"]):
    for _ in range(10):
        print(f"Current offset: {params['offset']}")
        params["offset"] += 1
        response = requests.request(method, apiURL, headers=headers, data=body, params=params)
        print(response.json())



# total_images = response.headers.get('Total-Count')
# print(f"Total image count: {total_images}")

# print("\n--- Response Details ---")
# print(f"Status Code: {response.status_code}")



# print("\n--- Response Body ---")
# try:
#     json_response = response.json()
#     print(json.dumps(json_response, indent=2))
# except json.JSONDecodeError:
#     print("Response is not JSON. Raw content:")
#     print(response.text)

