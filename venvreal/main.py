import requests

CHEAPSHARK_API_DEALS = "https://www.cheapshark.com/api/1.0/deals"
CHEAPSHARK_API_STORES = "https://www.cheapshark.com/api/1.0/stores"
CHEAPSHARP_REDIRECT = "https://www.cheapshark.com/redirect?dealID="
store_response_init = requests.get(url=CHEAPSHARK_API_STORES)
store_response_init.raise_for_status()
store_response_init_json = store_response_init.json()
print(store_response_init_json)
deals_params = {
    "sortBy": "Price"
}
cheapshark_response = requests.get(url=CHEAPSHARK_API_DEALS, params=deals_params)
cheapshark_response.raise_for_status()
cheapshark_response_json = cheapshark_response.json()
print(cheapshark_response_json)


def search_game(user_game_title):
    game_params = {
        'title': user_game_title,
        'sortBy': 'Price'
    }
    cheapshark_response = requests.get(url=CHEAPSHARK_API_DEALS, params=game_params)
    cheapshark_response.raise_for_status()
    cheapshark_response_json = cheapshark_response.json()
    print(cheapshark_response_json)
    for game in cheapshark_response_json:
        if float(game['salePrice']) < float(game['normalPrice']):
            for store in store_response_init_json:
                if game['storeID'] in store['storeID']:
                    print(f"Title: {game['title']}\n"
                          f"Store Name: {store['storeName']}\n"
                          f"Normal Price: {game['normalPrice']}\n"
                          f"Sale Price: {game['salePrice']}\n"
                          f"Link: {CHEAPSHARP_REDIRECT + game['dealID']}")
        else:
            pass


def deal_lookup(user_deal):
    CHEAPSHARK_API_DEAL_LOOKUP = f"https://www.cheapshark.com/api/1.0/deals?id={user_deal}"
    print(CHEAPSHARP_REDIRECT+user_deal)
    deal_details_response = requests.request("GET", CHEAPSHARK_API_DEAL_LOOKUP)
    deal_details_response.raise_for_status()
    deal_details_response_json = deal_details_response.json()
    print(deal_details_response_json)


running = True
while running:
    user_input = input("Get deals press g\nGet List of Stores press s\nGet deal details press d\n")
    if user_input.lower() == 'g':
        running_game_title = True
        while running_game_title:
            game_title = input("Are you looking for a specific game title?\ny/n\n")
            if game_title.lower() == 'n':
                print(cheapshark_response_json)
                for games in cheapshark_response_json:
                    for store in store_response_init_json:
                        if games['storeID'] in store['storeID']:
                            print(f"Title: {games['title']}\n"
                                  f"Store Name: {store['storeName']}\n"
                                  f"Normal Price: {games['normalPrice']}\n"
                                  f"Sale Price: {games['salePrice']}\n"
                                  f"Link: {CHEAPSHARP_REDIRECT + games['dealID']}")
                running_game_title = False
            elif game_title.lower() == 'y':
                user_game_title = input("What's the game title you'd liek to search for?\n")
                search_game(user_game_title)
                running_game_title = False
            else:
                print("I didnt understand your choice. Please try again.")
    elif user_input.lower() == 's':
        print(store_response_init_json)
    elif user_input.lower() == 'd':
        user_deal = input("Please enter the deal ID: \n")
        deal_lookup(user_deal)
    else:
        print("I dont know what that is. Please try again.\n")
