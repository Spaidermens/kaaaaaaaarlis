import requests
import time

# Your Discogs user token
USER_TOKEN = "cZUCErFtXvqrRMpDLGyiBBkOpeingyoaByIKlGxK"

# Discogs API base URL
BASE_URL = "https://api.discogs.com"

# Headers for authentication
headers = {
    "Authorization": f"Discogs token={USER_TOKEN}",
    "User-Agent": "WantlistTracker/1.0"  # ASCII-only
}

def get_wantlist(username):
    """Fetch the user's wantlist."""
    endpoint = f"{BASE_URL}/users/{username}/wants"
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching wantlist: {e}")
        return None

def get_lowest_listing_price(release_id):
    """Fetch the lowest priced listing for a release using /marketplace/search."""
    endpoint = f"{BASE_URL}/marketplace/search"
    params = {"release_id": release_id, "sort": "price", "sort_order": "asc"}
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"No listings found for release {release_id}.")
        else:
            print(f"Error fetching listings for release {release_id}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching listings for release {release_id}: {e}")
        return None

def track_wantlist(username):
    """Track and display the lowest prices for items in the wantlist."""
    wantlist = get_wantlist(username)
    if not wantlist:
        print("No wantlist found or error fetching wantlist.")
        return

    print(f"Tracking wantlist for user: {username}")
    for item in wantlist.get("wants", []):
        release_id = item["id"]
        release_title = item.get("basic_information", {}).get("title", "Unknown Title")
        artist_name = item.get("basic_information", {}).get("artists", [{}])[0].get("name", "Unknown Artist")

        print(f"Checking release: {artist_name} - {release_title} (ID: {release_id})")

        listings_data = get_lowest_listing_price(release_id)
        if listings_data and "results" in listings_data and listings_data["results"]:
            lowest_price = listings_data["results"][0]["price"]["value"]
            print(f"Lowest Price: ${lowest_price}")
        else:
            print("No listings found or error fetching listings.")
        print("-" * 40)


YOUR_USERNAME = "ClearMilk"

if __name__ == "__main__":
    while True:
        track_wantlist(YOUR_USERNAME)
        time.sleep(3600)  # Check every hour