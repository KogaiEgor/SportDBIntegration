import requests


API_BASE_URL = "https://www.thesportsdb.com/api/v1/json/3/"


def fetch_from_api(endpoint: str, params: dict = None) -> dict:
    url = f"{API_BASE_URL}{endpoint}"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_countries_from_api():
    data = fetch_from_api("all_countries.php")
    if "countries" not in data:
        raise ValueError("Invalid API response: Missing 'countries' key")
    return data["countries"]


def get_leagues_from_api(country_name):
    data = fetch_from_api("search_all_leagues.php", {"c": country_name})
    if "countries" not in data:
        raise ValueError("Failed to fetch leagues: Missing 'countries' key")
    return data["countries"]


def get_teams_from_api(league_name):
    data = fetch_from_api("search_all_teams.php", {"l": league_name})
    if "teams" not in data:
        raise ValueError("Failed to fetch teams: Missing 'teams' key")
    return data["teams"]
