from django.db import models

#from profile.models import UserProfile
from basecat.models import Base, Bootstrap


class Publication(Bootstrap):
    #profile = models.ForeignKey(UserProfile)
    authors = models.CharField(max_length=512, blank=True)
    publisher = models.CharField(max_length=512, blank=True)
    date_published = models.DateTimeField(blank=True)

class Page(Bootstrap):
    pub = models.ManyToManyField(Publication, blank=True, related_name='page_of_publication')
    tracking = models.CharField(max_length=255)
    number = models.IntegerField(default=0)
    image = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u"%s" % self.name