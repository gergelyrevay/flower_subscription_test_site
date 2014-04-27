import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase
from signup.views import SignupCreate, SignupCreateWithQuestionaire
from django.test import RequestFactory

class SignupViewsBasicTestCase(TestCase):
    fixtures = ['signup_testdata.json']

    def test_signup_load(self):
        url = reverse("signup")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_signup_with_questionaire_load(self):
        url = reverse("signup_with_questionaire")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

class SignupViewsPostTestCase(TestCase):
    fixtures = ['signup_testdata.json']

    def test_signup_create_success(self):
        """ submitting the simple signup form results a
        redirect to the same url and the message is success
        """
        # the response is a redirect to the same url
        url = reverse("signup")
        resp = self.client.post(url, {'email_address': 'test@example.com', 'feedback_text':'aaaaaaaaaaaaa'}, follow=True)
        self.assertRedirects(resp, url)

        # the massege added to the new page is of type 'success'
        message = list(resp.context['messages'])[0]
        self.assertEqual(message.tags, u'success')

    def test_signup_create_existing_email(self):
        """ submitting the simple signup form with an existing email
        address results in the same form with an error message
        """
        # the response is a redirect to the same url
        url = reverse("signup")
        resp = self.client.post(url, {'email_address': 'aaa@bbb.ccc', 'feedback_text':'aaaaaaaaaaaaa'})
        self.assertEqual(resp.status_code, 200)

        # Checks error message for the email address.
        self.assertFormError(resp, 'form', 'email_address', 'Signup with this Email address already exists.')

class SignupWithQuestionaireViewsTestCase(TestCase):
    fixtures = ['signup_testdata.json']

    def setup_view(self, view, request, *args, **kwargs):
        """Mimic as_view() returned callable, but returns view instance.
        args and kwargs are the same you would pass to ``reverse()``
        """
        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view

    def test_get_context_data(self):
        """SignupCreateWithQuestionaire.get_context_data() sets 'name' in context."""
        # Setup request and view.
        request = RequestFactory().post('/signupwithquestionaire',
            data={'email_address':'test222@example.com',
                'feedback_text':'aaaaaaaaaaaaa',
                'How do you feel yourself?':'Good',
                'What is your name?':'Little Bobby Tables'}
                ,)
        view = SignupCreateWithQuestionaire()
        view = self.setup_view(view, request)
        # Run.
        context = view.get_context_data()
        # Check that the two forms are equal.
        # import ipdb; ipdb.set_trace()
        form_in_view = (list(SignupCreateWithQuestionaire.get_form(view ,view.form_class)))
        form_in_context = (list(context['form']))
        self.assertEqual(len(form_in_view), len(form_in_context))
        for i in range(len(form_in_view)):
            self.assertEqual(form_in_view[i].name, form_in_context[i].name)
        # Check that the signup form also exist and equal in the context
        signup_form_in_view = (list(SignupCreateWithQuestionaire.get_form(view ,view.signup_form_class)))
        signup_form_in_context = (list(context['signup_form']))
        self.assertEqual(len(signup_form_in_view), len(signup_form_in_context))
        for i in range(len(signup_form_in_view)):
            self.assertEqual(signup_form_in_view[i].name, signup_form_in_context[i].name)

    def test_signup_create_with_questionaire_success(self):
        """ submitting the simple signup form results a
        redirect to the same url and the message is success
        """
        # the response is a redirect to the same url
        url = reverse("signup")
        resp = self.client.post(url, {'email_address': 'test@example.com', 'feedback_text':'aaaaaaaaaaaaa'}, follow=True)
        self.assertRedirects(resp, url)

        # the massege added to the new page is of type 'success'
        message = list(resp.context['messages'])[0]
        self.assertEqual(message.tags, u'success')

    def test_signup_create_with_questionaire_existing_email(self):
        """ submitting the simple signup form with an existing email
        address results in the same form with an error message
        """
        # the response is a redirect to the same url
        url = reverse("signup")
        resp = self.client.post(url, {'email_address': 'aaa@bbb.ccc', 'feedback_text':'aaaaaaaaaaaaa'})
        self.assertEqual(resp.status_code, 200)

        # Checks error message for the email address.
        self.assertFormError(resp, 'form', 'email_address', 'Signup with this Email address already exists.')
