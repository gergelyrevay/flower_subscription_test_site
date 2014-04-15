# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FAQ'
        db.create_table(u'faq_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faq_question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('faq_answer', self.gf('django.db.models.fields.TextField')()),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'faq', ['FAQ'])


    def backwards(self, orm):
        # Deleting model 'FAQ'
        db.delete_table(u'faq_faq')


    models = {
        u'faq.faq': {
            'Meta': {'object_name': 'FAQ'},
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'faq_answer': ('django.db.models.fields.TextField', [], {}),
            'faq_question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['faq']