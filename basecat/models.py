from django.db import models
from django.template.defaultfilters import slugify

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_column="DateAdded", editable=False)
    modified = models.DateTimeField(auto_now=True, db_column="DateModified", editable=False)

    class Meta:
        abstract = True

class Bootstrap(Base):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=False)
    desc=models.TextField(blank=True,null=True)
    slug=models.SlugField(blank=True)
    active=models.BooleanField(default=False)

    def __unicode__(self):
        return "%d) %s" % (self.id, self.name)

    def get_absolute_url(self):
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Bootstrap, self).save(*args, **kwargs)

    class Meta:
        abstract = True
