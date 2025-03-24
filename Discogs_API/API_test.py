import requests


USER_TOKEN = "cZUCErFtXvqrRMpDLGyiBBkOpeingyoaByIKlGxK"


BASE_URL = "https://api.discogs.com"

headers = {
    "Authorization": f"Discogs token={USER_TOKEN}",
    "User-Agent": "MyDiscogsApp/1.0"  
}

def test_discogs_api():
   
    endpoint = f"{BASE_URL}/oauth/identity"

    try:
        # API request
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  

        #response JSON
        user_data = response.json()
        print("API Test Successful!")
        print("User Information:")
        print(f"Username: {user_data.get('username')}")
        print(f"Profile URL: {user_data.get('resource_url')}")

    except requests.exceptions.RequestException as e:
        print("Error testing Discogs API:", e)

#tests
if __name__ == "__main__":
    test_discogs_api()