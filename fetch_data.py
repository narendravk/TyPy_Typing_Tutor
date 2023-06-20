import requests
import random
API_ENDPOINT="https://api.npoint.io/cebe6ad6d827b0ae51a3"

def fetch_data():
    response = requests.get(url=API_ENDPOINT)
    response.raise_for_status()
    data=response.json()
    return(random.choice(data["data"]))


def setup_game(player_name:str):
    try:
        with open(file="saved_data.txt",mode="r") as file:
            content = file.read()
    except FileNotFoundError:
        with open(file="saved_data.txt",mode="w") as file:
            content = f"{player_name}:0"
            file.write(content)
    finally:
        data_list = content.split(":")
        return data_list

def record_high_score(player_name,player_score):
    with open(file="saved_data.txt", mode="r") as file:
        content = file.read()
        data_list = content.split(":")
    if int(data_list[1]) < int(player_score):
        with open(file="saved_data.txt",mode="w") as file:
            file.write(f"{player_name}:{int(player_score)}")
