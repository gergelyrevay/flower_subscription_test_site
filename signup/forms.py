from django import forms
from models import Signup, Questionaire
import ipdb

class SignupForm(forms.ModelForm):
    """basic form for signup"""

    class Meta:
        model = Signup
        fields = ['email_address','feedback_text']

class SignupWithQuestionaireForm(forms.Form):
    """ Signup form with the questionarie together.
    """
    signup_form = None

    def __init__(self, *args, **kwargs):
        """ Add a field for every question.
            Field may be CharField or ChoiceField; field name is question.order.
        """
        super(SignupWithQuestionaireForm, self).__init__(*args, **kwargs)

        questionaire = Questionaire.objects.filter(is_active=True).get()

        for question in questionaire.questions.all():

            choices = question.choices
            kw      = dict()


            if choices:
                # if choices are given it is a choice field
                answer_field  = forms.ChoiceField
                choices       = [c.strip() for c in choices.split(',')]
                kw["choices"] = [(c,c) for c in choices]
            else:
                # if no choices were given it is a freetext
                answer_field     = forms.CharField
                kw["max_length"] = 200

            self.fields[question.question_text] = answer_field(**kw)




