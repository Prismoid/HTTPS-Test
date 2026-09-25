import requests
import time

response = requests.get("https://localhost:10250", verify="certs/server.crt", cert=("certs/user1.crt", "certs/user1.key"))
print(response.text)

response = requests.get("https://localhost:10250", verify="certs/server.crt", cert=("certs/user2.crt", "certs/user2.key"))
print(response.text)

# response = requests.get("https://localhost:10250", verify="certs/server.crt")
# print(response.text)

# response = requests.get("https://localhost:10250")
# print(response.text)
