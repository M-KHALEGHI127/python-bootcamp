import requests 

responde = requests.get("https://v1/udf/history")
responde.raise_for_status()
data = responde.json()
print(data)