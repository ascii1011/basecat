# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publication'
        db.create_table(u'mediacenter_publication', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_column='DateAdded', blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_column='DateModified', blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'mediacenter', ['Publication'])

        # Adding model 'Page'
        db.create_table(u'mediacenter_page', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_column='DateAdded', blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_column='DateModified', blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tracking', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mediacenter', ['Page'])

        # Adding M2M table for field pub on 'Page'
        m2m_table_name = db.shorten_name(u'mediacenter_page_pub')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'mediacenter.page'], null=False)),
            ('publication', models.ForeignKey(orm[u'mediacenter.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'publication_id'])


    def backwards(self, orm):
        # Deleting model 'Publication'
        db.delete_table(u'mediacenter_publication')

        # Deleting model 'Page'
        db.delete_table(u'mediacenter_page')

        # Removing M2M table for field pub on 'Page'
        db.delete_table(db.shorten_name(u'mediacenter_page_pub'))


    models = {
        u'mediacenter.page': {
            'Meta': {'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'DateAdded'", 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'DateModified'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'page_of_publication'", 'blank': 'True', 'to': u"orm['mediacenter.Publication']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'tracking': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mediacenter.publication': {
            'Meta': {'object_name': 'Publication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'DateAdded'", 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'DateModified'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['mediacenter']