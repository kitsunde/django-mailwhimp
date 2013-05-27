# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table(u'mailwhimp_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=36)),
        ))
        db.send_create_signal(u'mailwhimp', ['Application'])

        # Adding model 'List'
        db.create_table(u'mailwhimp_list', (
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailwhimp.Application'])),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('default_from_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('default_from_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('default_from_subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mailwhimp', ['List'])

        # Adding model 'Campaign'
        db.create_table(u'mailwhimp_campaign', (
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mailwhimp.Application'])),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=30, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('send_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mailwhimp', ['Campaign'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table(u'mailwhimp_application')

        # Deleting model 'List'
        db.delete_table(u'mailwhimp_list')

        # Deleting model 'Campaign'
        db.delete_table(u'mailwhimp_campaign')


    models = {
        u'mailwhimp.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mailwhimp.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailwhimp.Application']"}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mailwhimp.list': {
            'Meta': {'object_name': 'List'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailwhimp.Application']"}),
            'default_from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'default_from_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'default_from_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mailwhimp']