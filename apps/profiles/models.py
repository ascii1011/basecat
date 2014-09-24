from django.db import models
from django.contrib.auth.models import User
from django.db.models.loading import get_model

from basecat.models import Bootstrap


class UserProfile(Bootstrap):
    """
    Multiple profiles: max 4 right now
    """
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __unicode__(self):
        return self.user.username

    @property
    def my_project_list(self):
        return get_model('projects', 'project').objects.filter(participants__in=[self])