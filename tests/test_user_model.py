import unittest
from typing import Any
from datetime import datetime

from apps.main import redis_store,mongo
from apps.main.service.auth.user_service import register_user
from apps.main.model.user import User,PydanticObjectId
from tests.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_encode_auth_token(self):
        user = User(username = 'test1',email='test@test.com', password='test')
        user['registered_on'] = datetime.utcnow()
        
        #Create user
        result = mongo.db.users.insert_one(user.to_bson())
        print(result)
        user.id = str(PydanticObjectId(result.inserted_id)) 
        # Save user to redis_store
        redis_store.hmset(user.id, user.to_bson())

        auth_token = user.encode_auth_token(identity=user.id)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User(username = "test1",email='test@test.com', password='test')
        user['registered_on'] = datetime.utcnow()
        #Create user
        result = mongo.db.users.insert_one(user)
        user.id = str(PydanticObjectId(result.inserted_id)) 
        # Save user to redis_store
        redis_store.hmset(user.id, user.to_bson())

        auth_token = user.encode_auth_token(identity=user.id)
        self.assertTrue(isinstance(auth_token, str))
        
        # Decode the token using flask_jwt_extended
        data = user.decode_auth_token(identity=user.id)#get_jwt_identity()
        self.assertEqual(data, user.id)


if __name__ == '__main__':
    unittest.main()

