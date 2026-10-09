import requests

response = requests.get("https://api.github.com")
print(response.status_code)   # 200 means OK
print(response.json())
