from django.db import models


class DescriptionsMixin(models.Model):
    strDescriptionEN = models.TextField(blank=True, null=True, verbose_name="Description (EN)")
    strDescriptionDE = models.TextField(blank=True, null=True, verbose_name="Description (DE)")
    strDescriptionFR = models.TextField(blank=True, null=True, verbose_name="Description (FR)")
    strDescriptionIT = models.TextField(blank=True, null=True, verbose_name="Description (IT)")
    strDescriptionCN = models.TextField(blank=True, null=True, verbose_name="Description (CN)")
    strDescriptionJP = models.TextField(blank=True, null=True, verbose_name="Description (JP)")
    strDescriptionRU = models.TextField(blank=True, null=True, verbose_name="Description (RU)")
    strDescriptionES = models.TextField(blank=True, null=True, verbose_name="Description (ES)")
    strDescriptionPT = models.TextField(blank=True, null=True, verbose_name="Description (PT)")
    strDescriptionSE = models.TextField(blank=True, null=True, verbose_name="Description (SE)")
    strDescriptionNL = models.TextField(blank=True, null=True, verbose_name="Description (NL)")
    strDescriptionHU = models.TextField(blank=True, null=True, verbose_name="Description (HU)")
    strDescriptionNO = models.TextField(blank=True, null=True, verbose_name="Description (NO)")
    strDescriptionPL = models.TextField(blank=True, null=True, verbose_name="Description (PL)")
    strDescriptionIL = models.TextField(blank=True, null=True, verbose_name="Description (IL)")

    class Meta:
        abstract = True


class MediaMixin(models.Model):
    strWebsite = models.URLField(max_length=500, blank=True, null=True, verbose_name="Website")
    strFacebook = models.URLField(max_length=500, blank=True, null=True, verbose_name="Facebook")
    strInstagram = models.URLField(max_length=500, blank=True, null=True, verbose_name="Instagram")
    strTwitter = models.URLField(max_length=500, blank=True, null=True, verbose_name="Twitter")
    strYoutube = models.URLField(max_length=500, blank=True, null=True, verbose_name="YouTube")
    strRSS = models.URLField(max_length=500, blank=True, null=True, verbose_name="RSS Feed")

    class Meta:
        abstract = True


class GraphicsMixin(models.Model):
    strFanart1 = models.URLField(max_length=500, blank=True, null=True, verbose_name="Fanart 1")
    strFanart2 = models.URLField(max_length=500, blank=True, null=True, verbose_name="Fanart 2")
    strFanart3 = models.URLField(max_length=500, blank=True, null=True, verbose_name="Fanart 3")
    strFanart4 = models.URLField(max_length=500, blank=True, null=True, verbose_name="Fanart 4")
    strBanner = models.URLField(max_length=500, blank=True, null=True, verbose_name="Banner URL")
    strBadge = models.URLField(max_length=500, blank=True, null=True, verbose_name="Badge URL")
    strLogo = models.URLField(max_length=500, blank=True, null=True, verbose_name="Logo URL")

    class Meta:
        abstract = True


class GeneralInfoMixin(models.Model):
    strSport = models.CharField(max_length=100, verbose_name="Sport Type")
    strGender = models.CharField(max_length=10, blank=True, null=True, verbose_name="Gender")
    strLocked = models.CharField(max_length=50, blank=True, null=True, verbose_name="Locked Status")

    class Meta:
        abstract = True
