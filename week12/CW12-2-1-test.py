import requests as rq

response1 = rq.get("http://192.168.1.167:8080/")
print(response1.json())

response2 = rq.post("http://192.168.1.167:8080/", json={"id": 1, "title": "HOME", "description": "clean the house"})
print(response2.text)

response3 = rq.get("http://192.168.1.167:8080/")
print(response3.json())

response4 = rq.post("http://192.168.1.167:8080/", json={"id": 2, "title": "DOGS", "description": "feed the dogs"})
print(response4.text)

response5 = rq.get("http://192.168.1.167:8080/")
print(response5.json())

