from django.core.exceptions import ObjectDoesNotExist
from ..models import Country, League, Team


def get_country(country):
    try:
        return Country.objects.get(name_en=country)
    except ObjectDoesNotExist:
        raise ValueError(f"Страна {country} не найдена в бд")


def get_league(league):
    try:
        return League.objects.get(strLeague=league)
    except ObjectDoesNotExist:
        raise ValueError(f"Лига {league} не найдена в бд")


def get_existing_leagues_for_country(country):
    return set(League.objects.filter(strCountry=country).values_list("idLeague", flat=True))


def get_existing_teams_for_league(league):
    return set(Team.objects.filter(strLeague=league).values_list("idTeam", flat=True))
