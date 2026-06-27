# =========================================================
# REQUESTS MODULE IN PYTHON
# =========================================================

# requests module is used to send HTTP requests
# to APIs or websites.

# Mainly used for:
# 1. GET request  -> fetch data
# 2. POST request -> send data
# 3. PUT request  -> update data
# 4. DELETE       -> delete data

# install module

# pip install requests


import requests


# GET request example

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

# print(response.text)
print(response.json())


# POST request example

data = {
"userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

response = requests.post(
            "https://jsonplaceholder.typicode.com/posts/1",
            json=data
          )

print(response.status_code)


# Real use cases:

# Calling REST API

# Fetching weather data

# API integration

# Web scraping

