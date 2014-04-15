from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    """ Admin for the FAQ table.
    """
    fields = ('faq_question', 'faq_answer', 'enabled')
    list_display = ['faq_question', 'faq_answer', 'enabled']

admin.site.register(FAQ, FAQAdmin)