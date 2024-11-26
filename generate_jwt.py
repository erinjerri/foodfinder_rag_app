import time
import jwt
import requests
from autogen import tool
from config import DOORDASH_DEVELOPER_ID, DOORDASH_KEY_ID, DOORDASH_SIGNING_SECRET

@tool
def doordash_create_delivery(delivery_details: dict) -> dict:
    """
    Tool to create a delivery request using the DoorDash Drive API.

    Parameters:
    - delivery_details (dict): Details of the delivery request.

    Returns:
    - dict: JSON response from DoorDash API.
    """
    # Generate JWT
    now = int(time.time())
    payload = {
        'aud': 'doordash',
        'iss': DOORDASH_DEVELOPER_ID,
        'kid': DOORDASH_KEY_ID,
        'exp': now + 3600,
        'iat': now,
    }
    token = jwt.encode(payload, DOORDASH_SIGNING_SECRET, algorithm='HS256', headers={'dd-ver': 'DD-JWT-V1'})

    # DoorDash Drive API endpoint
    url = 'https://openapi.doordash.com/drive/v2/deliveries'

    # Set headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=delivery_details)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None