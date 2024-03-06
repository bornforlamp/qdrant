import json
import requests
from tabulate import tabulate

# Function to recursively get bottom level keys and values from JSON data
def get_bottom_level(data, path='', bottom_levels=None):
    if bottom_levels is None:
        bottom_levels = []

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                get_bottom_level(value, f'{key}', bottom_levels)
            else:
                bottom_levels.append((f'{key}', value))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            get_bottom_level(item, f'{index}', bottom_levels)
    return bottom_levels

# URL to fetch JSON data from
url = 'http://localhost:6333/collections/test_collection/cluster'

# Fetch JSON data from URL
response = requests.get(url)
if response.status_code == 200:
    json_data = response.json()

    # Get bottom level keys and values
    bottom_levels = get_bottom_level(json_data)

    # Add headers to the data
    headers = ["Key", "Value"]

    # Format data as a list of lists for tabulate
    data_as_lists = [[key, value] for key, value in bottom_levels]

    # Print tabulated data
    print(tabulate(data_as_lists, headers=headers, tablefmt='grid'))
else:
    print("Error fetching data. Status code:", response.status_code)
