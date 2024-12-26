from django.contrib import admin
from .models import Country, League, Team


class CountryFilter(admin.SimpleListFilter):
    title = "Country"
    parameter_name = "country"

    def lookups(self, request, model_admin):
        countries = Country.objects.all()
        return [(country.id, country.name_en) for country in countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(strLeague__strCountry__id=self.value())
        return queryset


class LeagueFilter(admin.SimpleListFilter):
    title = "League"
    parameter_name = "league"

    def lookups(self, request, model_admin):
        country_id = request.GET.get("country")
        if country_id:
            leagues = League.objects.filter(strCountry__id=country_id)
            return [(league.id, league.strLeague) for league in leagues]
        return []

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(strLeague__id=self.value())
        return queryset


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name_en",)
    search_fields = ("name_en",)


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("strLeague", "strCountry")
    list_filter = ("strCountry",)
    search_fields = ("strLeague", "strCountry__name_en")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("strTeam", "strLeague")
    search_fields = ("strTeam", "strLeague__strLeague")
    list_filter = (CountryFilter, LeagueFilter)
