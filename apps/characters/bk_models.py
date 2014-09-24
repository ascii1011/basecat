from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from basecat.models import Base

"""
journal
storage = bags, pockets
equiped
race
Klass
#users
"""
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



class Race(Base):
    name = models.CharField( max_length=30 )

    def __unicode__(self):
        return "%d) %s" % (self.id, self.name)


class Klass(Base):
    name = models.CharField( max_length=30 )

    def __unicode__(self):
        return "%d) %s" % (self.id, self.name)


class Character(Base):
    id = models.AutoField( primary_key=True )
    session = models.CharField(max_length=50)
    name = models.CharField( max_length=30 )
    klass = models.ForeignKey(Klass, db_column="ClassID", blank=True, null=True)
    race = models.ForeignKey(Race, db_column="RaceID", blank=True, null=True)
    level = models.PositiveIntegerField(default=1)
    exp = models.PositiveIntegerfield(default=10)
    desc = models.TextField()
    slug = models.SlugField(blank=True)

    def __unicode__(self):
        return "%d) %s" % (self.id, self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Character, self).save(*args, **kwargs)

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
