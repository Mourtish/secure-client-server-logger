import requests

url = "http://localhost:5000/log"

data = {
    "message": "Unauthorized login attempt"
}

response = requests.post(url, json=data)

print(response.json())
