import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://670f9def-fda6-4002-8eb9-d80d7d1eedd4.westeurope.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '6PqH3kKgKgp8akL9dkEbdbddaJlRP0Kh'

# Two sets of data to score, so we get two results back
data = {
  "Inputs": {
    "data":
    [
      {
        "age": 17,
        "job": "blue-collar",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "balance": 529,            
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "day": 5,
        "month": "may",
        "duration": 971,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure"
      },
      {
        "age": 87,
        "job": "blue-collar",
        "marital": "married",
        "education": "tertiary",
        "default": "no",
        "balance": -171,            
        "housing": "yes",
        "loan": "yes",
        "contact": "cellular",
        "day": 5,
        "month": "may",
        "duration": 471,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure"
      },
    ]
  }  
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
