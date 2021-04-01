from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
# Create your tests here.

User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):    # python built in unit tests
        user_a = User(username='killray', email='killray@gmai.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = "some_password1"
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEquals(user_count, 1)
        self.assertNotEqual(user_count, 0)


    def test_user_password(self):
        # user_qs = User.objects.filter(username__iexact = 'killray')
        # user_exists = user_qs.exists() and user_qs.count() == 1
        # self.assertTrue(user_exists)
        # user_a = user_qs.first()
        self.assertTrue(self.user_a.check_password(self.user_a_pw))     # gives same result as combined lines 30,31,32,33

    def test_login_url(self):
        # login_url = '/login/'
        # self.assertEquals(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # python request - manage.py runserver
        # self.client.get, self.client.post
        # response = self.client.post(login_url,{},follow=True)
        data = {
            "username":"killray",
            "password": "some_password1"
        }
        response = self.client.post(login_url,data,follow=True)
        # print(dir(response))
        # print(response.request)
        status_code = response.status_code
        redirect_path = response.request.get('PATH_INFO')
        # self.assertEquals(redirect_path,settings.LOGIN_REDIRECT_URL)
        self.assertEquals(status_code, 200)




