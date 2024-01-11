from datetime import datetime
from games.api.http_request import get


class OpenCriticService:

    def __init__(self, app_key):
        self.base_url = "https://opencritic-api.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": app_key,
            "X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
        }


    def get_upcoming_releases(self) -> dict:
        response = get(url=f"{self.base_url}/game/upcoming", headers=self.headers)
        for game in response:
            game["firstReleaseDate"] = datetime.strptime(
                game["firstReleaseDate"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ).strftime("%d %B %Y")
        return response

    def get_recently_released_games(self) -> dict:
        response = get(url=f"{self.base_url}/game/recently-released", headers=self.headers)

        for game in response:
            game["firstReleaseDate"] = datetime.strptime(
                game["firstReleaseDate"], "%Y-%m-%dT%H:%M:%S.%fZ"
            ).strftime("%d %B %Y")

        return response

    def get_game_by_id(self, game_id):
        response = get(url=f"{self.base_url}/game/{game_id}", headers=self.headers)
        return response
