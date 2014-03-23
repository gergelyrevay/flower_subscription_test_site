from django.db import models
# from django.core.urlresolvers import reverse

# Create your models here.
class Signup(models.Model):
	signed_up_at = models.DateTimeField(auto_now_add=True, editable=False)
	email_address = models.EmailField()
	feedback_text = models.TextField()
	# questionaire = models.ForeignKey(Questionaire, related_name='signup')

# defines ordering
	class Meta:
		ordering = ['-signed_up_at', 'email_address']

	def __unicode__(self):
		return self.email_address

	def save(self, *args, **kwargs):
		super(Signup, self).save(*args, **kwargs)

	# def get_absolute_url(self):
		# return reverse('signup-detail', kwargs=('pk':self.pk))
		
# class Question(models.Model):
# 	question_text = models.CharField(max_length=200)
# 	answer = models.TextField()

# class Answer(models.Model):
# 	answer_text = models.TextField()

# # FIXME how to do such think as various answer types and stuff

# class FreeTextAnswer(Answer):
# 	#FIXME is anything needed here?

# class MultiChoiceAnswer(Answer):
# 	possible_answers = [] #FIXME what should this be
# 	choosen_answer = models.TextField()
# 	is_more_answer_allowed = models.Boolean() #FIXME does this exist?

# class Questionaire(models.Model):
# 	questions = [] #how to create list of Question()
# 	answer = [] # how to create a list of Answer()