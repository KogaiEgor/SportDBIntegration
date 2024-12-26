from django.http import JsonResponse
from SportsDB_app.services.services import save_countries_to_db, save_leagues_to_db, save_teams_to_db
from SportsDB_app.services.api_clients import get_countries_from_api, get_leagues_from_api, get_teams_from_api


API_BASE_URL = "https://www.thesportsdb.com/api/v1/json/3/"


def get_countries(request):
    try:
        countries_data = get_countries_from_api()
        created_count = save_countries_to_db(countries_data)
        return JsonResponse({"created": f"Added {created_count} new countries"}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e)}, status=500)


def get_leagues_by_country(request):
    country_name = request.GET.get("country")
    if not country_name:
        return JsonResponse({"error": "Country parameter is required"}, status=400)

    try:
        leagues_data = get_leagues_from_api(country_name)
        created_count = save_leagues_to_db(leagues_data, country_name)
        return JsonResponse({"created": created_count}, status=200)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def get_teams_by_league(request):
    league_name = request.GET.get("league_name")
    if not league_name:
        return JsonResponse({"error": "League name parameter is required"}, status=400)

    try:
        teams_data = get_teams_from_api(league_name)
        created_count = save_teams_to_db(teams_data, league_name)
        return JsonResponse({"created": created_count}, status=200)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
