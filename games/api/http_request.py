import requests

from games.util.log_util import get_logger

log = get_logger()


def get(url: str, headers: dict):
    try:
        response = requests.get(url=url, headers=headers, timeout=20)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        log.error(f"HTTP request error: {error}")
        return None
