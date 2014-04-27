import datetime
from django.test import TestCase
from signup.models import Signup, Question, Answer, Questionaire


class SignupTestCase(TestCase):
    fixtures = ['signup_testdata.json']

    def setUp(self):
        super(SignupTestCase, self).setUp()
        self.signup_3 = Signup.objects.get(pk=3)
        self.question_3 = Question.objects.get(pk=3)
        self.answer_3 = Answer.objects.get(pk=3)
        self.questionaire_3 = Questionaire.objects.get(pk=3)

    def test_signup_loads(self):
        # data can be loaded from signup
        self.assertEqual(self.signup_3.email_address, 'aaa@bbb.ccc')
        # data can be loaded from question
        self.assertEqual(self.question_3.question_text, 'What is your name?')
        # data can be loaded from answer
        self.assertEqual(self.answer_3.answer_text, 'good') 
        # data can be loaded from questionaire
        self.assertEqual(self.questionaire_3.name, 'third questionaire') 