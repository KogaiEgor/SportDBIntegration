from django.db import transaction
from .querries import get_country, get_league, get_existing_leagues_for_country, get_existing_teams_for_league
from .utils import fill_model_with_validation
from ..models import Country, League, Team


def save_countries_to_db(countries_data):
    existing_countries = set(Country.objects.values_list("name_en", flat=True))
    new_countries = []

    for country_data in countries_data:
        if country_data.get("name_en") not in existing_countries:
            new_countries.append(
                Country(
                    name_en=country_data.get("name_en"),
                    flag_url_32=country_data.get("flag_url_32"),
                )
            )

    with transaction.atomic():
        Country.objects.bulk_create(new_countries)

    return len(new_countries)


def save_leagues_to_db(leagues_data, country):
    country_instance = get_country(country)
    existing_leagues_ids = get_existing_leagues_for_country(country_instance)
    new_leagues = []

    for league_data in leagues_data:
        league_id = league_data.get("idLeague")
        if league_id not in existing_leagues_ids:
            new_league = fill_model_with_validation(League, league_data)
            new_league.strCountry = country_instance
            new_leagues.append(new_league)

    if new_leagues:
        with transaction.atomic():
            League.objects.bulk_create(new_leagues)

    return len(new_leagues)


def save_teams_to_db(teams_data, league):
    league_instance = get_league(league)
    country_instance = league_instance.strCountry
    existing_teams_id = get_existing_teams_for_league(league_instance)

    new_teams = []

    for team_data in teams_data:
        team_id = team_data.get("idTeam")
        if team_id not in existing_teams_id:
            new_team = fill_model_with_validation(Team, team_data)
            new_team.strCountry = country_instance
            new_team.strLeague = league_instance
            new_teams.append(new_team)

    if new_teams:
        with transaction.atomic():
            Team.objects.bulk_create(new_teams)

    return len(new_teams)
