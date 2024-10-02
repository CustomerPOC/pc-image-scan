import Python.modules.fetchToken as fetchToken;
import requests
import os;

url        = os.getenv("PRISMA_CLOUD_URL")
password   = os.getenv("PRISMA_CLOUD_SECRET")
username   = os.getenv("PRISMA_CLOUD_IDENTITY")
consoleURL = os.getenv("PRISMA_CLOUD_CONSOLE")

endpoint   = "v1/images"
method     = "POST"
body       = {}
params     = [
    "limit=1",
    "offset=0"
]

token   = fetchToken(url=url, password=password, username=username)
apiURL  = f"{consoleURL}/{endpoint}" + "&".join(params)
headers = {
    'Accept': 'application/json',
    'x-redlock-auth': token
}

data = (requests.request(method, apiURL, headers=headers, data=body)).json()

print(data)