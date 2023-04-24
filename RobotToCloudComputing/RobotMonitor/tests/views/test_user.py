from uuid import uuid4
from datetime import date, timedelta
from json import loads, JSONDecodeError
from pytz import UTC

from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.utils.timezone import now, datetime

from .. import test_utils
from ...models import FrontendUser
from ...views import user as user_views
from rest_framework_simplejwt.views import TokenRefreshView


class TestFrontendUserViews(TestCase):
    def test_create_user(self):
        """
        create_user endpoint accepts correclty formatted data and saves it correctly
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        request = factory.post('/RobotMonitor/user/create', user)
        response = user_views.CreateUser.as_view()(request)

        self.assertEqual(response.status_code, 200)
        frontend_user = FrontendUser.objects.get(pk=user['id'])
        self.assertEqual(frontend_user.is_superuser, False)
        self.assertEqual(frontend_user.is_staff, False)
        self.assertEqual(frontend_user.is_active, user['is_active'])
        self.assertEqual(frontend_user.email, user['email'])
        self.assertEqual(frontend_user.first_name, user['first_name'])
        self.assertEqual(frontend_user.last_name, user['last_name'])
        self.assertEqual(frontend_user.date_of_birth, user['date_of_birth'])
        
        self.assertTrue(hasattr(frontend_user, 'date_joined'))
        self.assertTrue(hasattr(frontend_user, 'date_modified'))
        self.assertTrue(hasattr(frontend_user, 'last_login'))
        
    def test_users_can_log_in_with_valid_credentials(self):
        """
        user_login endpoint works when request contains valid credentials
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        
        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request = factory.post('/RobotMonitor/user/user_login', credentials)
        response = user_views.UserLogin.as_view()(request)

        self.assertEqual(response.status_code, 200)
        decoded_response = response.content.decode('UTF-8')
        auth_data = loads(decoded_response)
        self.assertIn('refresh', auth_data)
        self.assertIn('access', auth_data)
        
    def test_users_cannot_log_in_with_invalid_credentials(self):
        """
        user_login endpoint fails when request contains invalid credentials
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        correct_email = user['email']
        correct_password = user['password']

        incorrect_email = test_utils.generate_random_email()
        incorrect_password = test_utils.generate_random_password()

        credentials_incorrect_email = {
            'email': incorrect_email, 'password': correct_password}
        credentials_incorrect_password = {
            'email': correct_email, 'password': incorrect_password}
        credentials_both_incorrect = {
            'email': incorrect_email, 'password': incorrect_password}

        request1 = factory.post(
            '/RobotMonitor/user/user_login', credentials_incorrect_email)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertIn(response1.status_code, (302, 401))

        false_positive = True
        try:
            decoded_response = response1.content.decode('UTF-8')
            auth_data = loads(decoded_response)
        except JSONDecodeError:
            false_positive = False
        self.assertFalse(false_positive)

        request2 = factory.post(
            '/RobotMonitor/user/user_login', credentials_incorrect_password)
        response2 = user_views.UserLogin.as_view()(request2)
        self.assertIn(response2.status_code, (302, 401))

        false_positive = True
        try:
            decoded_response = response2.content.decode('UTF-8')
            auth_data = loads(decoded_response)
        except JSONDecodeError:
            false_positive = False
        self.assertFalse(false_positive)

        request3 = factory.post('/RobotMonitor/user/user_login',
                                credentials_both_incorrect)
        response3 = user_views.UserLogin.as_view()(request3)
        self.assertIn(response3.status_code, (302, 401))

        false_positive = True
        try:
            decoded_response = response2.content.decode('UTF-8')
            auth_data = loads(decoded_response)
        except JSONDecodeError:
            false_positive = False
        self.assertFalse(false_positive)

    def test_users_can_access_data_with_jwt_access_token(self):
        """
        Users can authenticate and access data by sending access token in headers
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)

        self.assertEqual(response2.status_code, 200)

    def test_users_cannot_access_data_using_jwt_refresh_token(self):
        """
        Users cannot authenticate and access data by sending refresh token, rather than
        access token in headers
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['refresh']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)

        self.assertIn(response2.status_code, (302, 401, 403))

    def test_users_can_refresh_jwt_access_token(self):
        """
        refresh_token endpoint works correctly and returns new, valid access and refresh tokens
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)
        self.assertEqual(response2.status_code, 200)

        refresh_request_data = {'refresh': auth_data['refresh']}
        request3 = factory.post('/RobotMonitor/refresh_token', refresh_request_data)
        response3 = TokenRefreshView.as_view()(request3)
        self.assertEqual(response3.status_code, 200)

        decoded_response3 = response3.render().content.decode('UTF-8')
        new_auth_data = loads(decoded_response3)

        self.assertNotEqual(auth_data['access'], new_auth_data['access'])
        self.assertNotEqual(auth_data['refresh'], new_auth_data['refresh'])

        auth_header = {
            'HTTP_AUTHORIZATION': f'Bearer {new_auth_data["access"]}'}
        request4 = factory.get('/RobotMonitor/user/get', **auth_header)
        response4 = user_views.GetUserData.as_view()(request4)
        self.assertEqual(response4.status_code, 200)

        refresh_request_data = {'refresh': new_auth_data['refresh']}
        request5 = factory.post('/RobotMonitor/refresh_token', refresh_request_data)
        response5 = TokenRefreshView.as_view()(request5)
        self.assertEqual(response5.status_code, 200)

    def test_jwt_refresh_token_blacklisted_after_use(self):
        """
        Refresh token blacklisted (no longer works) after use
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)
        self.assertEqual(response2.status_code, 200)

        refresh_request_data = {'refresh': auth_data['refresh']}
        request3 = factory.post('/RobotMonitor/refresh_token', refresh_request_data)
        response3 = TokenRefreshView.as_view()(request3)
        self.assertEqual(response3.status_code, 200)

        request4 = factory.post('/RobotMonitor/refresh_token', refresh_request_data)
        response4 = TokenRefreshView.as_view()(request4)
        self.assertIn(response4.status_code, (302, 401, 403))

    def test_jwt_refresh_token_blacklisted_after_logout(self):
        """
        Refresh token blacklisted (no longer works) after the user logs out
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)
        self.assertEqual(response2.status_code, 200)

        refresh_request_data = {'refresh': auth_data['refresh']}
        request3 = factory.post('/RobotMonitor/user/user_logout',
                                refresh_request_data, format='json')
        force_authenticate(
            request3, user=FrontendUser.objects.get(pk=user['id']))
        response3 = user_views.UserLogout.as_view()(request3)
        self.assertEqual(response3.status_code, 200)

        request4 = factory.post('/RobotMonitor/refresh_token', refresh_request_data)
        response4 = TokenRefreshView.as_view()(request4)
        self.assertIn(response4.status_code, (302, 401, 403))

    def test_unauthenticated_users_cannot_access_data(self):
        """
        Users cannot authenticate without an access token
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer"}
        request1 = factory.get('/RobotMonitor/user/get', **auth_header)
        response1 = user_views.GetUserData.as_view()(request1)
        self.assertIn(response1.status_code, (302, 401, 403))

        credentials = {'email': user['email'], 'password': user['password']}
        request2 = factory.post('/RobotMonitor/user/user_login', credentials)
        response2 = user_views.UserLogin.as_view()(request2)
        self.assertEqual(response2.status_code, 200)

        decoded_response2 = response2.content.decode('UTF-8')
        auth_data = loads(decoded_response2)

        request3 = factory.get('/RobotMonitor/user/get', **auth_header)
        response3 = user_views.GetUserData.as_view()(request3)
        self.assertIn(response3.status_code, (302, 401, 403))

    def test_get_public_key(self):
        """
        The get_public_key endpoint returns the public key and the future public key
        """
        factory = APIRequestFactory()

        request1 = factory.get('/RobotMonitor/get_public_key')
        response1 = user_views.GetPublicKey.as_view()(request1)
        self.assertEqual(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        key_data1 = loads(decoded_response1)

        self.assertIn('public_key', key_data1)

        request2 = factory.get('/RobotMonitor/get_public_key')
        response2 = user_views.GetPublicKey.as_view()(request2)
        self.assertEqual(response2.status_code, 200)

        decoded_response2 = response2.content.decode('UTF-8')
        key_data2 = loads(decoded_response2)

        self.assertEqual(key_data1, key_data2)

    def test_inactive_users_cannot_log_in(self):
        """
        Inactive users cannot log in, even with correct credentials
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        user['is_active'] = False
        create_request = factory.post('/RobotMonitor/user/create', user)
        user_views.CreateUser.as_view()(create_request)

        credentials = {'email': user['email'], 'password': user['password']}
        request = factory.post('/RobotMonitor/user/user_login', credentials)
        response = user_views.UserLogin.as_view()(request)

        self.assertIn(response.status_code, (302, 401))

    def test_last_login_updates_upon_login(self):
        """
        After login, FrontendUser.last_login field is updated
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)
        credentials = {'email': user['email'], 'password': user['password']}

        before_time = now()
        login_request = factory.post('/RobotMonitor/user/user_login', credentials)
        user_views.UserLogin.as_view()(login_request)
        after_time = now()

        request = factory.get('/RobotMonitor/user/get', format='json')
        force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))
        response = user_views.GetUserData.as_view()(request)

        decoded_response = response.content.decode('UTF-8')
        frontend_user = loads(decoded_response)

        last_login = UTC.localize(datetime.strptime(
            frontend_user['last_login'], '%Y-%m-%dT%H:%M:%S.%fZ'))

        self.assertGreater(last_login, before_time)
        self.assertLess(last_login, after_time)

    def test_last_login_defaults_to_account_creation_time(self):
        """
        When FrontendUser is first created, last_login is automatically set to the time 
        the user was created
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()

        before_time = now()
        test_utils.create_user(**user)
        after_time = now()

        request = factory.get('/RobotMonitor/user/get', format='json')
        force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))
        response = user_views.GetUserData.as_view()(request)

        decoded_response = response.content.decode('UTF-8')
        frontend_user = loads(decoded_response)

        last_login = UTC.localize(datetime.strptime(
            frontend_user['last_login'], '%Y-%m-%dT%H:%M:%S.%fZ'))

        self.assertGreater(last_login, before_time)
        self.assertLess(last_login, after_time)

    def test_users_can_change_password(self):
        """
        change_password endpoint changes user password and user can log in with new password
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)

        new_password = test_utils.generate_random_password()
        request_data = {
            'old_password': user['password'], 'new_password': new_password}
        change_password_request = factory.post(
            '/RobotMonitor/user/change_password', request_data, format='json')
        force_authenticate(change_password_request,
                           user=FrontendUser.objects.get(pk=user['id']))
        user_views.ChangePassword.as_view()(change_password_request)

        credentials = {'email': user['email'], 'password': new_password}
        request1 = factory.post('/RobotMonitor/user/user_login', credentials)
        response1 = user_views.UserLogin.as_view()(request1)
        self.assertTrue(response1.status_code, 200)

        decoded_response1 = response1.content.decode('UTF-8')
        auth_data = loads(decoded_response1)

        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}
        request2 = factory.get('/RobotMonitor/user/get', **auth_header)
        response2 = user_views.GetUserData.as_view()(request2)
        self.assertTrue(response2.status_code, 200)

        decoded_response2 = response2.content.decode('UTF-8')
        first_name = loads(decoded_response2)['first_name']

        self.assertEqual(first_name, user['first_name'])

    def test_users_cant_log_in_with_old_password(self):
        """
        After changing password with change_password endpoint, users cannot log in with old password
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)

        old_password = user['password']
        new_password = test_utils.generate_random_password()
        request_data = {'old_password': old_password,
                        'new_password': new_password}
        change_password_request = factory.post(
            '/RobotMonitor/user/change_password', request_data, format='json')
        force_authenticate(change_password_request,
                           user=FrontendUser.objects.get(pk=user['id']))
        user_views.ChangePassword.as_view()(change_password_request)

        logout_request = factory.get('/RobotMonitor/user/user_logout')
        user_views.UserLogout.as_view()(logout_request)

        credentials = {'email': user['email'], 'password': old_password}
        request = factory.post('/RobotMonitor/user/user_login', credentials)
        response = user_views.UserLogin.as_view()(request)
        self.assertIn(response.status_code, (302, 401, 403))

    def test_old_password_required_to_change_password(self):
        """
        change_password endpoint doesn't change password if old password is not correct
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)

        new_password = test_utils.generate_random_password()
        request_data = {
            'old_password': user['password'] + 'wrong_pass', 'new_password': new_password}
        request1 = factory.post(
            '/RobotMonitor/user/change_password', request_data, format='json')
        force_authenticate(
            request1, user=FrontendUser.objects.get(pk=user['id']))
        response1 = user_views.ChangePassword.as_view()(request1)
        self.assertIn(response1.status_code, (302, 401, 403))

        request_data = {'new_password': new_password}
        request2 = factory.post(
            '/RobotMonitor/user/change_password', request_data, format='json')
        force_authenticate(
            request1, user=FrontendUser.objects.get(pk=user['id']))
        response2 = user_views.ChangePassword.as_view()(request2)
        self.assertIn(response2.status_code, (302, 401, 403))

        factory.get('/RobotMonitor/logout')

        credentials = {'email': user['email'], 'password': new_password}
        request3 = factory.post('/RobotMonitor/user/user_login', credentials)
        response3 = user_views.UserLogin.as_view()(request3)
        self.assertIn(response3.status_code, (302, 401, 403))

    def test_user_stays_logged_in_after_password_change(self):
        """
        After password change, user is still logged in and can access data with previous JWT
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)

        credentials = {'email': user['email'], 'password': user['password']}
        login_request = factory.post('/RobotMonitor/user/user_login', credentials)
        login_response = user_views.UserLogin.as_view()(login_request)
        self.assertTrue(login_response.status_code, 200)

        decoded_response1 = login_response.content.decode('UTF-8')
        auth_data = loads(decoded_response1)
        auth_header = {'HTTP_AUTHORIZATION': f"Bearer {auth_data['access']}"}

        new_password = test_utils.generate_random_password()
        request_data = {
            'old_password': user['password'], 'new_password': new_password}
        change_password_request = factory.post(
            '/RobotMonitor/user/change_password', request_data, **auth_header)
        user_views.ChangePassword.as_view()(change_password_request)

        request = factory.get('/RobotMonitor/user/get', **auth_header)
        response = user_views.GetUserData.as_view()(request)
        self.assertTrue(response.status_code, 200)

        decoded_response = response.content.decode('UTF-8')
        display_name = loads(decoded_response)['first_name']

        self.assertEqual(display_name, user['first_name'])

    def test_get_user_data(self):
        """
        get_user_data endpoint correctly returns user data
        """
        factory = APIRequestFactory()

        user = test_utils.generate_random_user()
        test_utils.create_user(**user)

        request = factory.get('/RobotMonitor/user/get', format='json')
        force_authenticate(request, user=FrontendUser.objects.get(pk=user['id']))
        response = user_views.GetUserData.as_view()(request)
        self.assertEqual(response.status_code, 200)

        decoded_response = response.content.decode('UTF-8')
        frontend_user = loads(decoded_response)

        self.assertIsNotNone(frontend_user['date_joined'])
        self.assertIsNotNone(frontend_user['date_modified'])
        self.assertIsNotNone(frontend_user['last_login'])
        self.assertEqual(frontend_user['is_superuser'], False)
        self.assertIsNotNone(frontend_user['is_staff'], False)

        frontend_user.pop('date_joined')
        frontend_user.pop('date_modified')
        frontend_user.pop('last_login')
        frontend_user.pop('is_superuser')
        frontend_user.pop('is_staff')

        user['id'] = str(user['id'])
        user['date_of_birth'] = str(user['date_of_birth'])
        user.pop('password')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(frontend_user, user)
