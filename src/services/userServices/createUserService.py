from dotenv.main import load_dotenv
from domains.userDomain import UserDomain
from jsonschema import validate
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
import os


load_dotenv()


class createUserService:
    def validate(self, data, db, UsersModel):
        self.data = data
        self.db = db
        self.UsersModel = UsersModel

        schema = {
            "type": "object",
            "required": ["username", "password"],
            "properties": {
                "username": {
                    "type": "string",
                    "minLength": 5,

                },
                "password": {
                    "type": "string",
                    "minLength": 8,
                }
            },
            "additionalProperties": False
        }

        try:
            validate(data, schema)
        except Exception as e:
            return {"error": e.message}, 400

    def create(self):
        userAlreadyExist = UserDomain.find(self.data, self.db, self.UsersModel)

        if userAlreadyExist:
            return {"error": "Username already exists"}, 400

        self.data['password'] = generate_password_hash(self.data['password'])

        return UserDomain.create(self.data, self.db, self.UsersModel)

    def verifyPassword(self):
        user = UserDomain.find(self.data, self.db, self.UsersModel)

        if not user:
            return {"error": "invalid username or password"}, 400

        if(check_password_hash(user.password, self.data['password'])):
            token = jwt.encode({
                'public_id': user.id,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, os.environ['SECRET_KEY'])

            return {"token": token}

        else:
            return {"error": "invalid username or password"}, 400
