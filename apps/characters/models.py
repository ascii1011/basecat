from django.db import models

from basecat.models import Bootstrap
#from profile.models import UserProfile

class Race(Bootstrap): pass

class Klass(Bootstrap): pass

class Character(Bootstrap):
    #profile = models.ForeignKey(UserProfile)
    klass = models.ForeignKey(Klass, db_column="ClassObj", blank=True, null=True)
    race = models.ForeignKey(Race, db_column="RaceObj", blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    exp = models.PositiveIntegerField(default=10)