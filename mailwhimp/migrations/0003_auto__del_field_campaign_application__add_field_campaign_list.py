# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Campaign.application'
        db.delete_column(u'mailwhimp_campaign', 'application_id')

        # Adding field 'Campaign.list'
        db.add_column(u'mailwhimp_campaign', 'list',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['mailwhimp.List']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Campaign.application'
        raise RuntimeError("Cannot reverse this migration. 'Campaign.application' and its values cannot be restored.")
        # Deleting field 'Campaign.list'
        db.delete_column(u'mailwhimp_campaign', 'list_id')


    models = {
        u'mailwhimp.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mailwhimp.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailwhimp.List']"}),
            'send_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mailwhimp.list': {
            'Meta': {'object_name': 'List'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mailwhimp.Application']"}),
            'default_from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'default_from_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'default_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mailwhimp']