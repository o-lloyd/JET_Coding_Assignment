import requests

postcode = "TN173HN"

url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Print the HTTP status code
print(f"Status Code: {response.status_code}")
