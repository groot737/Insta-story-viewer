import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def searchUser(username):
    url = "https://instagram-stories1.p.rapidapi.com/get_user_id"

    querystring = {"username": f'{username}'}

    headers = {
        "X-RapidAPI-Key": os.getenv('api_key'),
        "X-RapidAPI-Host": "instagram-stories1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['user_id']