from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from basecat.models import Base, Bootstrap


class Account(Bootstrap):
    """
    these fields are only to be used on signin for bootstrapping session
    """
    user = models.OneToOneField(User)
    city = models.CharField(_("city"), max_length=20, blank=True)
    state = models.CharField(_("state"), max_length=20, blank=True)
    zip = models.CharField(_("zip code"), max_length=20, blank=True)
    website = models.URLField(_("website"), blank=True)
    max_profiles = models.IntegerField(default=4)
    profile_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

class Locale(models.Model):
    user = models.OneToOneField(Account)
    x = models.FloatField(blank=True)
    y = models.FloatField(blank=True)
    
class ConnectionInformation(models.Model):
    user = models.ForeignKey(Account)
    ip = models.GenericIPAddressField(null=True, default='0.0.0.0')
    sessionid = models.CharField(max_length=100, blank=True)

class UserAttributes(models.Model):
    pass
