import requests
from autogen import tool
from config import YELP_API_KEY

@tool
def yelp_search(location: str, category: str, term: str = None, limit: int = 5) -> dict:
    """
    Tool to search for businesses using the Yelp API.

    Parameters:
    - location (str): Location to search.
    - category (str): Business category.
    - term (str, optional): Search term.
    - limit (int, optional): Number of results to return.

    Returns:
    - dict: JSON response from Yelp API.
    """
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'Bearer {YELP_API_KEY}'}
    params = {
        'location': location,
        'categories': category,
        'term': term,
        'limit': limit
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None