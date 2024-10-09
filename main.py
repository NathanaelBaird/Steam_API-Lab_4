# main start
import pip._vendor.requests

import requests
import json

def search_steam_games(query, limit=5):
    url = "https://steam-api7.p.rapidapi.com/search"
    
    # Set the query and limit as parameters for the API request
    querystring = {"query": query, "limit": str(limit)}
    
    headers = {
        "x-rapidapi-key": "4065700c01msh806444439527cd5p1c6978jsn329732cf064b",
        "x-rapidapi-host": "steam-api7.p.rapidapi.com"
    }
    
    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response and print it in a formatted way
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage of the function
search_steam_games("Grand Theft", 5)

