import requests

POSTCODE = "M204AG"

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_restaurants(postcode):

    # Send GET request to the API
    response = requests.get(URL.format(postcode=postcode), headers=HEADERS)

    # If the GET request was successful
    if response.status_code == 200:

        # Turn json response into python dictionary
        data = response.json()

        # Get data of the first restaurants
        restaurants = data['restaurants']

        # If there are restaurants then return the first 10
        if restaurants is not None:
            return restaurants[:10]
        else:
            raise ValueError("API response did not contain any restaurant data.")

    # If GET request was unsuccessful
    else:
        print("Error: ", response.status_code)


def print_restaurants(postcode, restaurants):

    print(f"\nRestaurants near {postcode}:\n")
    print("-" * 50)

    for restaurant in restaurants:
        restaurant_name = restaurant.get('name', "Unknown")
        cuisines = restaurant.get("cuisines", [])
        star_rating = restaurant.get('rating', {}).get('starRating', 'No Rating')
        address = restaurant.get('address', {})

        print(f"\n{restaurant_name}")
        print("Cuisines:", ", ".join(cuisine.get('name') for cuisine in cuisines))
        print(f"Rating: {star_rating}")
        print(f"Address: {address.get('firstLine')}, {address.get('city')}, {address.get('postalCode')}\n")
        print("-" * 50)

def main():
    restaurants = get_restaurants(POSTCODE)

    if restaurants is not None:
        print_restaurants(POSTCODE, restaurants)

if __name__ == "__main__":
    main()