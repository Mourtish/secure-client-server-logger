import requests

url = "http://localhost:5000/log"

headers = {
    "X-API-KEY": "supersecretkey"
}

data = {
    "message": "Unauthorized login attempt"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())