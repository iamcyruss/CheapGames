import requests

CHEAPSHARK_API_DEALS = "https://www.cheapshark.com/api/1.0/deals"
CHEAPSHARK_API_STORES = "https://www.cheapshark.com/api/1.0/stores"
running = True


while running:
    user_input = input("Get deals press g\nGet List of Stores press s\nGet deal details press d\n")
    if user_input.lower() == 'g':
        running_game_title = True
        while running_game_title:
            game_title = input("Are you looking for a specific game title?\n(Y)es/(N)o\n")
            if game_title.lower() == 'n':
                cheapshark_response = requests.get(url=CHEAPSHARK_API_DEALS)
                cheapshark_response.raise_for_status()
                cheapshark_response_json = cheapshark_response.json()
                print(cheapshark_response_json)
                running_game_title = False
            elif game_title.lower() == 'y':
                user_game_title = input("What's the game title you'd liek to search for?\n")
                game_params = {
                    'title': user_game_title
                }
                cheapshark_response = requests.get(url=CHEAPSHARK_API_DEALS, params=game_params)
                cheapshark_response.raise_for_status()
                cheapshark_response_json = cheapshark_response.json()
                print(cheapshark_response_json)
                running_game_title = False
            else:
                print("I didnt understand your choice. Please try again.")
    elif user_input.lower() == 's':
        store_response = requests.get(url=CHEAPSHARK_API_STORES)
        store_response.raise_for_status()
        store_response_json = store_response.json()
        print(store_response_json)
    elif user_input.lower() == 'd':
        user_deal = input("Please enter the deal ID: \n")
        CHEAPSHARK_API_DEAL_LOOKUP = {
            "id": user_deal
        }
        print(CHEAPSHARK_API_DEAL_LOOKUP)
        deal_details_response = requests.get(url=CHEAPSHARK_API_DEALS, params=CHEAPSHARK_API_DEAL_LOOKUP)
        deal_details_response.raise_for_status()
        deal_details_response_json = deal_details_response.json()
        print(deal_details_response_json)
    else:
        print("I dont know what that is. Please try again.\n")
