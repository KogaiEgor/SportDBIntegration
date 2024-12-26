from django.db import models
from SportsDB_app.models_mixins import *


class Country(models.Model):
    name_en = models.CharField(max_length=255, unique=True, verbose_name="Country Name")
    flag_url_32 = models.URLField(max_length=500, blank=True, verbose_name="Flag URL")

    def __str__(self):
        return self.name_en


class League(DescriptionsMixin, MediaMixin, GraphicsMixin, GeneralInfoMixin):
    idLeague = models.CharField(max_length=50, unique=True, verbose_name="League ID")
    idSoccerXML = models.CharField(max_length=50, blank=True, null=True, verbose_name="Soccer XML ID")
    idAPIfootball = models.CharField(max_length=50, blank=True, null=True, verbose_name="API Football ID")
    idCup = models.CharField(max_length=50, blank=True, null=True, verbose_name="Cup ID")

    strLeague = models.CharField(max_length=255, verbose_name="League Name")
    strLeagueAlternate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Alternate Name")
    intDivision = models.IntegerField(blank=True, null=True, verbose_name="Division")
    strCurrentSeason = models.CharField(max_length=50, blank=True, null=True, verbose_name="Current Season")
    intFormedYear = models.IntegerField(blank=True, null=True, verbose_name="Formed Year")
    dateFirstEvent = models.DateField(blank=True, null=True, verbose_name="First Event Date")

    strPoster = models.URLField(max_length=500, blank=True, null=True, verbose_name="Poster URL")
    strTrophy = models.URLField(max_length=500, blank=True, null=True, verbose_name="Trophy URL")

    strTvRights = models.TextField(blank=True, null=True, verbose_name="TV Rights")
    strNaming = models.CharField(max_length=255, blank=True, null=True, verbose_name="Naming Format")
    strComplete = models.CharField(max_length=50, blank=True, null=True, verbose_name="Completion Status")

    strCountry = models.ForeignKey(
        Country, related_name="leagues", on_delete=models.CASCADE, verbose_name="Country"
    )

    def __str__(self):
        return f"{self.strLeague} ({self.strCountry.name_en})"


class Team(DescriptionsMixin, MediaMixin, GraphicsMixin, GeneralInfoMixin):
    idTeam = models.CharField(max_length=50, unique=True, verbose_name="Team ID")
    idESPN = models.CharField(max_length=50, blank=True, null=True, verbose_name="ESPN ID")
    idAPIfootball = models.CharField(max_length=50, blank=True, null=True, verbose_name="API Football ID")

    strTeam = models.CharField(max_length=255, verbose_name="Team Name")
    strTeamAlternate = models.CharField(max_length=255, blank=True, null=True, verbose_name="Alternate Name")
    strTeamShort = models.CharField(max_length=50, blank=True, null=True, verbose_name="Short Name")
    intFormedYear = models.IntegerField(blank=True, null=True, verbose_name="Formed Year")
    idVenue = models.CharField(max_length=50, blank=True, null=True, verbose_name="Venue ID")
    strStadium = models.CharField(max_length=255, blank=True, null=True, verbose_name="Stadium Name")
    strLocation = models.CharField(max_length=255, blank=True, null=True, verbose_name="Location")
    intStadiumCapacity = models.IntegerField(blank=True, null=True, verbose_name="Stadium Capacity")

    idLeague = models.CharField(max_length=50, blank=True, null=True, verbose_name="League ID")
    strLeague2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 2")
    idLeague2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 2 ID")
    strLeague3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 3")
    idLeague3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 3 ID")
    strLeague4 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 4")
    idLeague4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 4 ID")
    strLeague5 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 5")
    idLeague5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 5 ID")
    strLeague6 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 6")
    idLeague6 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 6 ID")
    strLeague7 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Additional League 7")
    idLeague7 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Additional League 7 ID")
    strDivision = models.CharField(max_length=255, blank=True, null=True, verbose_name="Division")

    strEquipment = models.URLField(max_length=500, blank=True, null=True, verbose_name="Equipment")

    intLoved = models.IntegerField(blank=True, null=True, verbose_name="Loved Count")
    strKeywords = models.CharField(max_length=500, blank=True, null=True, verbose_name="Keywords")
    strColour1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Primary Colour")
    strColour2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Secondary Colour")
    strColour3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tertiary Colour")

    strCountry = models.ForeignKey(
        Country, related_name="teams", on_delete=models.CASCADE, verbose_name="Country"
    )
    strLeague = models.ForeignKey(
        League, related_name="teams", on_delete=models.CASCADE, verbose_name="League"
    )

    def __str__(self):
        return f"{self.strTeam} ({self.strLeague.strLeague})"
