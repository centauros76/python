import requests

# GET
resp = requests.get("https://tech.kakaoenterprise.com/category/Tech%20Log")
print("GET TEXT :: {}".format(resp.text))
print("GET TEXT :: {}".format(resp.status_code))

# POST
dic = {"id":1, "name":"Kim", "age":10}
resp = requests.post("http://httpbin.org/post", data=dic)
print("POST TEXT :: {}".format(resp.text))

