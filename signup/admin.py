from django.contrib import admin

from .models import Signup

class SignupAdmin(admin.ModelAdmin):
	date_hierarchy = 'signed_up_at'
	fields = ('email_address', 'feedback_text')
	list_display = ['email_address', 'signed_up_at']
	list_display_link = ['email_address']
	#list_editable = ['email_address']
	#list_filter = ['']

admin.site.register(Signup, SignupAdmin)
