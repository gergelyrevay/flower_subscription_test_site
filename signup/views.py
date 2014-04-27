from django.shortcuts import render
from .models import Signup, Answer, Question
from django.views.generic.edit import CreateView, FormView
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from .forms import SignupWithQuestionaireForm, SignupForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


# functions are views
# def signup_list(request, *args, **kwargs):
#   signup_list = Signup.objects.all()
#   template_name = 'signup_list.html'

#   context = {
#       'signup_list': signup_list
#   }

#   return render(request, template_name, context)

class SignupCreate(SuccessMessageMixin, CreateView):
    """ SignupCreate gives a form to sign up and saves the submitted forms.
    It doesn't involve the questionaire.
    """
    model = Signup
    template_name = 'signup_form.html'
    fields = ['email_address','feedback_text']
    success_url = reverse_lazy('signup')
    success_message = 'The signup was successful, thank you!'


class SignupCreateWithQuestionaire(SuccessMessageMixin, FormView):
    """ Signup with additional questionaire. The Signup form and
    the questionaire form are created and validated separately.
    """
    form_class = SignupWithQuestionaireForm
    signup_form_class = SignupForm
    template_name = 'signup_with_questionaire_form.html'
    success_url = reverse_lazy('signup_with_questionaire')
    success_message = 'The signup was successful, thank you!'


    def get_context_data(self, **kwargs):
        """ Creates the two separate forms for the HTML template.
        """
        context = super(SignupCreateWithQuestionaire, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'signup_form' not in context:
            context['signup_form'] = self.signup_form_class()

        return context


    def forms_valid(self, question_form, signup_form):
        """ Saves both forms in the database.
        """
        question_data = question_form.cleaned_data
        signup = signup_form.save()

        # looks up questions in the question table to save their reference instead of the text
        for question_text in question_data.keys():
            question = Question.objects.filter(question_text = question_text).get()
            answer_text = question_data[question_text]
            answer = Answer(question=question, answer_text=answer_text, signup=signup)
            answer.save()

        context = self.get_context_data()
        return self.render_to_response()

    def forms_invalid(self):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """ Handle posts. Both forms are validated separately.
        If both is valid the data is saved in the database.
        """
        signup_form = self.get_form(self.signup_form_class)
        question_form = self.get_form(self.form_class)
        if question_form.is_valid() and signup_form.is_valid():
            return self.forms_valid(question_form=question_form, signup_form=signup_form)
        else:
            return self.forms_invalid()
