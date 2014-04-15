from django.shortcuts import render
from django.views.generic import ListView
from .models import FAQ

class FAQView(ListView):
    model = FAQ
    fields = ['faq_question','faq_answer']
    template_name = 'faq_list.html'

    def get_queryset(self):
        return FAQ.objects.filter(enabled=True)