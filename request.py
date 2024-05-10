import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"Total Deaths:"})

print(r.json())