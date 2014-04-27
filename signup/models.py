from django.db import models

class Signup(models.Model):
    """ Simple signup with email and free text feedback.
    """
    signed_up_at = models.DateTimeField(auto_now_add=True, editable=False)
    email_address = models.EmailField(unique=True)
    feedback_text = models.TextField()

# defines ordering
    class Meta:
        ordering = ['-signed_up_at', 'email_address']

    def __unicode__(self):
        return self.email_address

    def save(self, *args, **kwargs):
        super(Signup, self).save(*args, **kwargs)

    # def get_absolute_url(self):
        # return reverse('signup-detail', kwargs=('pk':self.pk))
        
class Question(models.Model):
    """ Question table. Answer can be freetext or multiplechoice,
    and choices can be defined.
    """
    question_text = models.CharField(max_length=200)
    choices = models.CharField(max_length=500, blank=True, null=True)
    answer_type = models.CharField(max_length=6, choices=((u"1", u"freetext"), (u"2", "multiplechoice")))

    def __unicode__(self):
        return self.question_text   

class Answer(models.Model):
    """ The final answers are stored here, connected to
    the question object and the particular signup where they were given.
    """
    answer_text = models.TextField()
    question = models.ForeignKey(Question, related_name="answers", blank=True, null=True)
    signup = models.ForeignKey(Signup, related_name="answers", blank=True, null=True)

class Questionaire(models.Model):
    """ Defined questionaires by ordering a set of question to it.
    Only one questionaire can be active at a time.
    """
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question)