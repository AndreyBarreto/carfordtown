from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from models.models import Models

#####Services######
from services.personServices.createPersonService import createPersonService
from services.carsServices.createCarService import createCarService
from services.userServices.createUserService import createUserService
#####Services######


####Instance Services####
CreatePerson = createPersonService()
CreateCar = createCarService()
CreateUser = createUserService()
####Instance Services####

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-secret2'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

(PeoplesModel, CarsModel, UsersModel) = Models.generate(db)


@app.route("/")
def home():
    return {"hello": "CarFord Town"}


@app.route("/people", methods=["POST"])
def create_person():
    data = request.json
    isNotValidJson = CreatePerson.validate(data)
    if isNotValidJson:
        return isNotValidJson

    return CreatePerson.create(data, db, PeoplesModel)


@app.route("/car/<id_people>", methods=["POST"])
def create_car(id_people):
    data = request.json
    isNotValidJson = CreateCar.validate(data)
    if isNotValidJson:
        return isNotValidJson

    return CreateCar.create(data, id_people, db, PeoplesModel, CarsModel)


@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    isNotValidJson = CreateUser.validate(data, db, UsersModel)
    if isNotValidJson:
        return isNotValidJson

    return CreateUser.create()


@app.route("/auth", methods=["POST"])
def get_token():
    data = request.json
    isNotValidJson = CreateUser.validate(data, db, UsersModel)
    if isNotValidJson:
        return isNotValidJson

    return CreateUser.verifyPassword()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)
