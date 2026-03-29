# JET_Coding_Assignment

A terminal application that retrieves data from the Just Eat API and displays information for 10 restaurants for a given postcode.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
```bash
   git clone 
   cd 
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

## Assumptions
- The restaurants did not need to be ordered by rating or distance from the postcode.
- User input for the postcode was not required but was added to avoid hardcoding a postcode.

## Improvements
- Remove non-food related descriptions from the cuisines output.
- Allow the user to re-enter a postcode if it is a valid format but is an invalid postcode, i.e. the API request does not return any restaurants.
