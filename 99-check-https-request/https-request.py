import requests
import time

response = requests.get("https://localhost:10250", verify="certs/server.crt", cert=("certs/user.crt", "certs/user.key"))
print(response.text)

# response = requests.get("https://localhost:10250", verify="certs/server.crt")
# print(response.text)

# response = requests.get("https://localhost:10250")
# print(response.text)
