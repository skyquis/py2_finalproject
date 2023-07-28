# Inputs
# Search criteria
# First and last name

# Outputs
# Stats

# Processing
# Input data validation
# Call to API using first and last name
# Clean up json output
# Output stats

# Imports
import requests


def api_search(player_name):

    # where to do player name validation?

    search_name = player_name

    # Search url to search for players by name from ball don't lie API
    search_url = f'https://www.balldontlie.io/api/v1/players?search={search_name}'

    # Call to API
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        # what happens if multiple players with same name?
        if data['data']:
            player_id = data['data'][0]['id']
            # Endpoint to get the player's stats by ID
            player_stats_url = f'https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}'
            response = requests.get(player_stats_url)
            if response.status_code == 200:
                player_stats = response.json()
                # Process and use the player's stats as needed
                print(player_stats)
            else:
                print("Failed to get player's stats.")
        else:
            print("Player not found.")
    else:
        print("Failed to get player information.")

    return player_stats


if __name__ == '__main__':
    lbj_stats = api_search('lebron james')
    # my_stats = api_search('skyler marquis')

