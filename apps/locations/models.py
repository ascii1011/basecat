from django.db import models
from basecat.models import Bootstrap

class LocationType(Bootstrap): 
    parent = models.PositiveIntegerField(null=True)
    
class LocationBase(Bootstrap):
    type = models.ForeignKey(LocationType, db_column="TypeObj", blank=True, null=True)

    def __unicode__(self):
        return "[%d.%s] %s" % ( self.id, str(self.type), self.name )