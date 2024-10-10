import Autocomplete
import Languages
import Search
import Short_Desc
import Total_apps

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Autocomplete Search")
        print("2. Get Supported Languages")
        print("3. Search Steam Games")
        print("4. Get Short Description")
        print("5. Get Total Apps")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            query = input("Enter game name for autocomplete: ")
            limit = input("Enter result limit (default 5): ")
            limit = limit if limit else 5
            Autocomplete.steam_autocomplete(query, limit)
        
        elif choice == "2":
            app_id = input("Enter the App ID (default 271590): ")
            plain_text = input("Plain Text (true/false, default true): ")
            lang = input("Language (default english): ")
            plain_text = plain_text if plain_text else "true"
            lang = lang if lang else "english"
            Languages.get_supported_languages(app_id, plain_text, lang)
        
        elif choice == "3":
            query = input("Enter game name to search: ")
            limit = input("Enter result limit (default 5): ")
            limit = limit if limit else 5
            Search.search_steam_games(query, limit)
        
        elif choice == "4":
            app_id = input("Enter the App ID (default 271590): ")
            plain_text = input("Plain Text (true/false, default true): ")
            lang = input("Language (default english): ")
            plain_text = plain_text if plain_text else "true"
            lang = lang if lang else "english"
            Short_Desc.get_short_description(app_id, plain_text, lang)
        
        elif choice == "5":
            Total_apps.get_total_steam_apps()
        
        elif choice == "6":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

