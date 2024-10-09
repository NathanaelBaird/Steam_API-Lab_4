import requests
import json

def get_short_description(app_id, plain_text="true", lang="english"):
    url = f"https://steam-api7.p.rapidapi.com/appDetails/shortDescription/{app_id}"
    
    # Query parameters for the request
    querystring = {"plainText": plain_text, "lang": lang}
    
    headers = {
        "x-rapidapi-key": "4065700c01msh806444439527cd5p1c6978jsn329732cf064b",
        "x-rapidapi-host": "steam-api7.p.rapidapi.com"
    }
    
    try:
        # Make the API request with query parameters
        response = requests.get(url, headers=headers, params=querystring)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse and print the response data
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
get_short_description("271590", plain_text="true", lang="english")
