import requests
import json

def steam_autocomplete(query, limit=5):
    url = "https://steam-api7.p.rapidapi.com/autocomplete"
    
    querystring = {"query": query, "limit": str(limit)}
    
    headers = {
        "x-rapidapi-key": "4065700c01msh806444439527cd5p1c6978jsn329732cf064b",
        "x-rapidapi-host": "steam-api7.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
