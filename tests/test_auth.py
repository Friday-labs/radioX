import unittest
import json
from base import BaseTestCase
from apps.main.service.auth.blacklist_service import save_token
from apps.main.model.blacklist_token import BlacklistedToken


def register_user(self):
    return self.client.post(
        '/user/register',
        data=json.dumps({
                'email': 'joe@example.com',
                'username': 'joe',
                'password': '123456'
            }),
            content_type='application/json'
        )


def login_user(self, registered=True):
    if registered:
        email = 'joe@example.com'
        password = '123456'
    else:
        email = 'not_registered@gmail.com'
        password = 'password'
    return self.client.post(
        '/auth/login',
        data=json.dumps({
            'email':email,
            'password':password
        }),
        content_type='application/json'
    )


class TestAuthBlueprint(BaseTestCase):
    def test_register(self):
        """Test user Registration"""
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_register_existing_user(self):
        """ Test Registration with registered email"""
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'User already exists. Please Log in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # registered user login
            response = login_user(self,registered=True)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        with self.client:
            response = login_user(self,registered=False)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'email or password does not match.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 401)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # user login
            resp_login = login_user(self,registered=True)
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['Authorization'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            # valid token logout
            response = self.client.post(
                '/auth/logout',
                headers={
                    'Authorization': 'Bearer ' + data_login['Authorization'][1]
                }
            )
            # print(response.data.decode())
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertEqual(response.status_code, 200)
    
    def test_valid_blacklisted_token_logout(self):
        """ Test for logout after a valid token gets blacklisted """
        with self.client:
            # user login
            resp_login = login_user(self,registered=True)
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['Authorization'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            # blacklist a valid token
            save_token(token=data_login['Authorization'][1])
            # blacklisted valid token logout
            response = self.client.post(
                '/auth/logout',
                headers={
                    'Authorization': 'Bearer ' + data_login['Authorization'][1]
                }
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Token Expired. Please log in again.')
            self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
