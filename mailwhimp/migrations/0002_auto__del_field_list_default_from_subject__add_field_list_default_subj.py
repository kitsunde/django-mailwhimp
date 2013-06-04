# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'List.default_from_subject'
        db.rename_column(u'mailwhimp_list',
                         'default_from_subject',
                         'default_subject')

    def backwards(self, orm):
        db.rename_column(u'mailwhimp_list',
                         'default_subject',
                         'default_from_subject')


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
            'default_subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mailwhimp']