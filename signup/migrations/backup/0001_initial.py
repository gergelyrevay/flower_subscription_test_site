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
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('feedback_text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'signup', ['Signup'])

        # Adding model 'Question'
        db.create_table(u'signup_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('answer_type', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'signup', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'signup_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer_text', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='answers', null=True, to=orm['signup.Question'])),
            ('signup', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='answers', null=True, to=orm['signup.Signup'])),
        ))
        db.send_create_signal(u'signup', ['Answer'])

        # Adding model 'Questionaire'
        db.create_table(u'signup_questionaire', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'signup', ['Questionaire'])

        # Adding M2M table for field questions on 'Questionaire'
        m2m_table_name = db.shorten_name(u'signup_questionaire_questions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('questionaire', models.ForeignKey(orm[u'signup.questionaire'], null=False)),
            ('question', models.ForeignKey(orm[u'signup.question'], null=False))
        ))
        db.create_unique(m2m_table_name, ['questionaire_id', 'question_id'])


    def backwards(self, orm):
        # Deleting model 'Signup'
        db.delete_table(u'signup_signup')

        # Deleting model 'Question'
        db.delete_table(u'signup_question')

        # Deleting model 'Answer'
        db.delete_table(u'signup_answer')

        # Deleting model 'Questionaire'
        db.delete_table(u'signup_questionaire')

        # Removing M2M table for field questions on 'Questionaire'
        db.delete_table(db.shorten_name(u'signup_questionaire_questions'))


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