from django.contrib import admin
from django import forms
from .models import Signup, Questionaire, Answer, Question



class SignupAdmin(admin.ModelAdmin):
    date_hierarchy = 'signed_up_at'
    fields = ('email_address', 'feedback_text')
    list_display = ['email_address', 'signed_up_at']
    list_display_link = ['email_address']
    #list_editable = ['email_address']
    #list_filter = ['']

class QuestionaireForm(forms.ModelForm): 
    """Custom form for Questionaires to show questions
    instead of the ObjectX reference.
    """
    def __init__(self, *args, **kwargs):
        super(QuestionaireForm, self).__init__(*args, **kwargs)
        question_list = Question.objects.all()
        questions_widget = self.fields['questions'].widget
        choices = []
        for choice in question_list:
            choices.append((choice.id, choice.question_text))
        questions_widget.choices = choices

class QuestionaireAdmin(admin.ModelAdmin):
    """Admin form for questionaires."""
    fields = ('is_active','name','questions',)
    list_display = ['name', 'is_active']
    form = QuestionaireForm


class AnswerAdmin(admin.ModelAdmin):
    """Admin form for Answers"""
    fields = ('question', 'signup','answer_text',)
    list_display = ['question', 'signup','answer_text']

class QuestionAdmin(admin.ModelAdmin):
    """Admin form for questions"""
    fields = ('question_text','choices','answer_type',)
    list_display = ['question_text', 'choices', 'answer_type']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Signup, SignupAdmin)
admin.site.register(Questionaire, QuestionaireAdmin)
admin.site.register(Answer, AnswerAdmin)
