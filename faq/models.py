from django.db import models

class FAQ(models.Model):
    """ Frequenty asked questions and answers. Only enabled questions are shown.
    """
    faq_question = models.CharField(max_length=200)
    faq_answer = models.TextField()
    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.faq_question