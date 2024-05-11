import requests

endpoint = "http://localhost:8000/api/products/1"

data = {
    "title":"This field is done"
}

get_response =  requests.get(endpoint , json = data)
print(requests)
print(get_response.json())



