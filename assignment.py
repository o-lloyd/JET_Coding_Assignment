import requests

postcode = "M204AG"

url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send GET request to the API
response = requests.get(url, headers=headers)

# If the GET request was successful
if response.status_code == 200:
    # Turn json response into python dictionary
    data = response.json()

    # Get data of the first ten restaurants
    restaurants = data['restaurants'][:10]

    print(f"Restaurants near {postcode}:\n")

    for restaurant in restaurants:
        print({restaurant['name']})
        print(f"Cuisines: {restaurant['cuisines']}")
        print(f"Rating: {restaurant['rating']['starRating']}")
        print(f"Address: {restaurant['address']}\n")
