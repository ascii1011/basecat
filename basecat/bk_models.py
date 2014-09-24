from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


LOCATION_TYPES=(
    ('reality', 'Alternate Reality'),
    ('dimension', 'Alertnate Dimension'),
    ('galaxy','Galaxy'),
    ('universe', 'Universe'),
    ('planet', 'Planet'),
    ('star', 'Star'),
    ('satellite', 'Satellite'),
    ('realm', 'Realm'),
    ('continent', 'Continent'),
    ('country', 'Country'),
    ('state', 'State'),
    ('city', 'City'),
    ('catacomb', 'Catacomb'),
    ('structure', 'Structure'), #parents, children, plural, definitions, geospacial, synonyms, 
    ('floor', 'Floor'),
    ('room', 'Room'), # categories: hall, closet, directions, self, etc...
    )


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_column="DateAdded", editable=False)
    modified = models.DateTimeField(auto_now=True, db_column="DateModified", editable=False)

    class Meta:
        abstract = True


class Bootstrap(Base):
    id = models.AutoField( primary_key=True )
    parent = models.PositiveIntegerField(null=True)
    name=models.CharField( max_length=100 )
    desc=models.TextField()
    slug=models.SlugField(blank=True)

    def __unicode__(self):
        return "%d) %s" % (self.id, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bootstrap, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class LocationType(Bootstrap): 
    pass
    
class LocationBase(Bootstrap):
    type = models.ForeignKey(LocationType, db_column="Type", blank=True, null=True)

    def __unicode__(self):
        return "[%d.%s] %s" % ( self.id, str(self.type), self.name )
        
    #class Meta:
        #ordering = (name)

#users
#characters
  #stats, gear, bag, look, leveling(experience, tools, weapons, etc), relationships, quests, behavior, environment demener

#locations

#group events


"""
class Words(Base):
    pass

class Docs(Base):
    pass
"""
#user = models.ForeignKey(User, unique=True, db_column="UserID")
#company = models.ManyToManyField(Company, db_column="Companies")
#company = models.ForeignKey(Company, db_column="CompanyID")
