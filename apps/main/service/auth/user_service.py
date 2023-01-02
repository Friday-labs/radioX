from datetime import datetime
# from . import users
from apps.main import mongo
from ...model.objectid import PydanticObjectId
from ...model.user import User


def register_new_user(data):
    user = mongo.db.users.find_one_or_404({"email":data['email']})
    if not user:
        user_details = data
        user_details["date_added"] = datetime.utcnow()
        new_user = User(
            **user_details
            )
        insert_result = mongo.db.users.insert_one(new_user.to_bson())
        new_user.id = PydanticObjectId(str(insert_result.inserted_id))
        print(new_user)

        return new_user.to_json()
        # return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409