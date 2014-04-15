# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Questionaire.name'
        db.add_column(u'signup_questionaire', 'name',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Questionaire.name'
        db.delete_column(u'signup_questionaire', 'name')


    models = {
        u'signup.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'signup.question': {
            'Meta': {'object_name': 'Question'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Answer']"}),
            'answer_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'signup.questionaire': {
            'Meta': {'object_name': 'Questionaire'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['signup.Question']", 'symmetrical': 'False'})
        },
        u'signup.signup': {
            'Meta': {'ordering': "['-signed_up_at', 'email_address']", 'object_name': 'Signup'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'feedback_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signed_up_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['signup']