import requests
import random
API_ENDPOINT="https://api.npoint.io/cebe6ad6d827b0ae51a3"

def fetch_data():
    response = requests.get(url=API_ENDPOINT)
    response.raise_for_status()
    data=response.json()
    return(random.choice(data["data"]))

