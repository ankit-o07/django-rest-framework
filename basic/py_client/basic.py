import requests

# endpoint = "https://www/github.com"
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


# get_response =  requests.get(endpoint)
# get_response =  requests.get(endpoint, data={"query":"this is a test text"})
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
get_response =  requests.post(endpoint,json={"title":"Hello World45"})

print(get_response.json())



