import requests

endpoint = "http://localhost:8000/api/products/8"

data = {
    "title":"This field is done"
}

get_response =  requests.get(endpoint , json = data)
print(get_response.json())



