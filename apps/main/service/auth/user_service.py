from datetime import datetime
# from . import users
from apps.main import mongo
from ...model.objectid import PydanticObjectId
from ...model.user import User


def register_new_user(data):
    user = mongo.db.users.find_one({"email":data['email']})
    if not user:
        user_details = data
        user_details["date_added"] = datetime.utcnow()
        new_user = User(
            **user_details
            )
        insert_result = mongo.db.users.insert_one(new_user.to_bson())
        new_user.id = str(PydanticObjectId(str(insert_result.inserted_id)))
        new_user.to_json()
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409