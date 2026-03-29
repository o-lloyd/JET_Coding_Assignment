# JET_Coding_Assignment

A Python console application that fetches restaurant data from the Just Eat API 
based on a UK postcode and displays the top 10 restaurants, including their 
name, cuisines, rating, and address.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/o-lloyd/JET_Coding_Assignment.git
   cd JET_Coding_Assignment
```

2. Install the required dependency:
```bash
   pip install requests
```

## How to Run
```bash
python assignment.py
```

You will be prompted to enter a UK postcode, or you can press `Enter` to use the default postcode (`M20 4AG`).
```
Enter a UK postcode, or press 'Enter' to use 'M204AG':
```

### Example Output
```
Restaurants near M20 4AG:

--------------------------------------------------

Nabzys - Withington
Cuisines: Chicken, Pizza, Halal, Local Legends, Collect stamps, Deals
Rating: 5
Address: 426 WILMSLOW ROAD, MANCHESTER, M20 3BW

--------------------------------------------------
```
## Notes
- The Just Eat API requires a User-Agent header to return a valid JSON response.

## Assumptions
- The restaurants did not need to be ordered by rating or distance from the postcode.
- User input for the postcode was not required but was added to avoid hardcoding a postcode.

## Improvements
- Remove non-food related descriptions from the cuisines output.
- Allow the user to re-enter a postcode if the postcode is non-existant.
- Allow the user to select a preferred cuisine type to filter the restaurants.
- Output the data in a web application. This would have been my desired way to show the data for a better user experience, but I am unfamiliar with how to implement this. This would be something I am keen to develop further.
