from django.db import models

from basecat.models import Base, Bootstrap


class Project(Bootstrap):
    participants = models.ManyToManyField('profiles.UserProfile', blank=True, related_name='project_participant_set')
    

    def __unicode__(self):
        return u"%s" % self.name