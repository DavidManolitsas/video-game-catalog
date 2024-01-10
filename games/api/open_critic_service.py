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
        return response
