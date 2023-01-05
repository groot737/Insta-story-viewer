import requests
import creeds

def searchUser(username):
    url = "https://instagram-stories1.p.rapidapi.com/get_user_id"

    querystring = {"username": f'{username}'}

    headers = {
        "X-RapidAPI-Key": f"{creeds.api_key}",
        "X-RapidAPI-Host": "instagram-stories1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # return response.json()['user_id']
    return response.json()

def searchStory(id):
    url = "https://instagram-scraper2.p.rapidapi.com/stories"

    querystring = {"user_id": f"{id}"}

    headers = {
        "X-RapidAPI-Key": f"{creeds.api_key}",
        "X-RapidAPI-Host": "instagram-scraper2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()
