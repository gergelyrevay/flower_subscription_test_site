from django.shortcuts import render
from .models import Signup
from django.views.generic.edit import CreateView
# from django.core.urlresolver import reverse_lazy
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy

# functions are views
def signup_list(request, *args, **kwargs):
	signup_list = Signup.objects.all()
	template_name = 'signup_list.html'

	context = {
		'signup_list': signup_list
	}

	return render(request, template_name, context)

# SignupCreate gives a form to sign up and saves the submitted forms
class SignupCreate(CreateView):
	model = Signup
	template_name = 'signup_form.html'
	fields = ['email_address','feedback_text']
	success_url = reverse_lazy('signup')