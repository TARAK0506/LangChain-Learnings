import requests

response = requests.post(
    "http://localhost:8000/chat",
    json = {
      "user_input": "My Name is Tarak?",
      "language": "italian"
      }
)
print(response.json())