# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Signup'
        db.create_table(u'signup_signup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signed_up_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('feedback_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'signup', ['Signup'])


    def backwards(self, orm):
        # Deleting model 'Signup'
        db.delete_table(u'signup_signup')


    models = {
        u'signup.signup': {
            'Meta': {'ordering': "['-signed_up_at', 'email_address']", 'object_name': 'Signup'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'feedback_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signed_up_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['signup']