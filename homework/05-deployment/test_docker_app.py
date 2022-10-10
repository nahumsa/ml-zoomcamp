import requests

url = "http://0.0.0.0:8000/predict"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
print(requests.post(url, json=client).json())
