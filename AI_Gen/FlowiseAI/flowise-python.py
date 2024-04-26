import requests

API_URL = "http://localhost:3010/api/v1/prediction/f99a1945-64ae-4e39-93ae-46c272e2b584"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "turkey",
})


###python3 flowise-python.py