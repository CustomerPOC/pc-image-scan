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
    "limit": 100,
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

total_images = response.headers.get('Total-Count')
print(f"Total image count: {total_images}")

if total_images is None:
    print("No images found.")
    exit()

total_images = int(total_images)
all_results = []  

while params["offset"] < total_images:
    print(f"Fetching records {params['offset']} to {params['offset'] + params['limit']}")
    
    response = requests.request(method, apiURL, headers=headers, data=body, params=params)
    current_data = response.json()
    
    # Add current batch to all results
    all_results.extend(current_data)
    
    # Increment offset for next batch
    params["offset"] += params["limit"]

print(f"Retrieved {len(all_results)} total records")


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
