from django.urls import path
from . import views


urlpatterns = [
    path("get_countries/", views.get_countries, name="get_countries"),
    path("get_leagues_by_country/", views.get_leagues_by_country, name="fetch_leagues_by_country"),
    path("get_teams_by_league/", views.get_teams_by_league, name="fetch_teams_by_league"),
]
