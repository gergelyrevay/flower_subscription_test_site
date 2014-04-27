# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Question.answer'
        db.delete_column(u'signup_question', 'answer_id')

        # Adding field 'Questionaire.is_active'
        db.add_column(u'signup_questionaire', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Answer.question'
        db.add_column(u'signup_answer', 'question',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='answers', null=True, to=orm['signup.Question']),
                      keep_default=False)

        # Adding field 'Answer.signup'
        db.add_column(u'signup_answer', 'signup',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='answers', null=True, to=orm['signup.Signup']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Question.answer'
        db.add_column(u'signup_question', 'answer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['signup.Answer']),
                      keep_default=False)

        # Deleting field 'Questionaire.is_active'
        db.delete_column(u'signup_questionaire', 'is_active')

        # Deleting field 'Answer.question'
        db.delete_column(u'signup_answer', 'question_id')

        # Deleting field 'Answer.signup'
        db.delete_column(u'signup_answer', 'signup_id')


    models = {
        u'signup.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer_text': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'answers'", 'null': 'True', 'to': u"orm['signup.Question']"}),
            'signup': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'answers'", 'null': 'True', 'to': u"orm['signup.Signup']"})
        },
        u'signup.question': {
            'Meta': {'object_name': 'Question'},
            'answer_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'signup.questionaire': {
            'Meta': {'object_name': 'Questionaire'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
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