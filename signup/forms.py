from django import forms
from models import Signup

class SignupForm(object):
	"""basic form for signup"""
	model = Signup
	fields = ['email_address','feedback_text']
