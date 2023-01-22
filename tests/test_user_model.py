import unittest
from typing import Any
from datetime import datetime

from apps.main import redis_store,mongo
from apps.main.service.auth.user_service import register_user
from apps.main.model.user import User
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_encode_auth_token(self):
        data = {'username':'test1','email':'test@test.com', 'password':'test','registered_on':datetime.utcnow()}
        user = User(**data)
        #Create user
        result = mongo.db.users.insert_one(data)
        # Save user to redis_store
        # redis_store.hmset(user.id, user.to_bson())
        auth_token = user.encode_auth_token(user_id=result.inserted_id)
        print(auth_token)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        data = {'username':'test1','email':'test@test.com', 'password':'test','registered_on':datetime.utcnow()}
        user = User(**data)
        #Create user
        result = mongo.db.users.insert_one(data)
        # Save user to redis_store
        # redis_store.hmset(user.id, user.to_bson())

        auth_token = user.encode_auth_token(result.inserted_id)
        self.assertTrue(isinstance(auth_token, str))
        
        # Decode the token using flask_jwt_extended
        data = user.decode_auth_token(auth_token)#get_jwt_identity()
        self.assertEqual(data, result.inserted_id)


if __name__ == '__main__':
    unittest.main()

