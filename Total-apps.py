import requests
import json

#with or without parameters

def get_total_steam_apps(query_params=None):
    url = "https://steam-api7.p.rapidapi.com/totalApps"
    
    headers = {
        "x-rapidapi-key": "4065700c01msh806444439527cd5p1c6978jsn329732cf064b",
        "x-rapidapi-host": "steam-api7.p.rapidapi.com"
    }
    
    try:
        # Make the API request, passing query parameters if provided
        response = requests.get(url, headers=headers, params=query_params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the response data
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage with and without query parameters:
# get_total_steam_apps()  # No query parameters

# Example with query parameters (you can customize this based on the API docs):
# For example, adding a "type" filter:
get_total_steam_apps(query_params={"type": "game"})
