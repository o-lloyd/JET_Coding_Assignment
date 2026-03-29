import requests
import re

BACKUP_POSTCODE = "M20 4AG" # If user does not input a postcode
POSTCODE_PATTERN = r'^[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}$' # Postcode input format
URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
HEADERS = {"User-Agent": "Mozilla/5.0"}
NO_OF_RESTAURANTS = 10

def format_postcode(postcode):
    # Formats the postcode with a space
    return f"{postcode[:-3]} {postcode[-3:]}"

def get_postcode_input():

    postcode = input(f"Enter a UK postcode, or press 'Enter' to use '{BACKUP_POSTCODE}': ").strip().upper()

    # Validate input is empty or in the required format
    while True:
        if not postcode:
            return BACKUP_POSTCODE.replace(" ", "")
        
        if not re.match(POSTCODE_PATTERN, postcode):
            postcode = input("Invalid postcode format, please re-enter:").strip().upper()
            continue

        return postcode.replace(" ", "")

def get_restaurants(postcode):

    response = requests.get(URL.format(postcode=postcode), headers=HEADERS)

    # If the GET request was successful
    if response.status_code == 200:

        data = response.json()

        restaurants = data['restaurants']

        # If there are no restaurants for that postcode
        if not restaurants:
            raise ValueError(f"No restaurants found near {format_postcode(postcode)}.")
        
        return restaurants[:NO_OF_RESTAURANTS]

    # If GET request was unsuccessful
    else:
        raise ValueError(f"Error: {response.status_code}")


def print_restaurants(postcode, restaurants):

    print(f"\nRestaurants near {format_postcode(postcode)}:\n")
    print("-" * 50)

    for restaurant in restaurants:
        restaurant_name = restaurant.get('name', "Unknown")
        cuisines = restaurant.get("cuisines", [])
        star_rating = restaurant.get('rating', {}).get('starRating', 'No Rating')
        address = restaurant.get('address', {})

        first_line = address.get('firstLine')
        city = address.get('city')
        postal_code = address.get('postalCode')

        print(f"\n{restaurant_name}")
        print("Cuisines:", ", ".join(cuisine.get('name') for cuisine in cuisines))
        print(f"Rating: {star_rating}")
        print(f"Address: {first_line}, {city}, {postal_code}\n")
        print("-" * 50)

def main():
    postcode = get_postcode_input()
    restaurants = get_restaurants(postcode)
    print_restaurants(postcode, restaurants)

if __name__ == "__main__":
    main()