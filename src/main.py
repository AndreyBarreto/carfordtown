from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from models.models import Models
from middlewares.authMiddleware import token_required

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

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

(PeoplesModel, CarsModel, UsersModel) = Models.generate(db)


@app.route("/")
def home():
    return {"hello": "CarFord Town"}


@app.route("/people", methods=["POST"])
@token_required
def create_person():
    data = request.json
    isNotValidJson = CreatePerson.validate(data, db, PeoplesModel)
    if isNotValidJson:
        return isNotValidJson

    return CreatePerson.create()


@app.route("/car/<id_people>", methods=["POST"])
@token_required
def create_car(id_people):
    data = request.json
    isNotValidJson = CreateCar.validate(
        data, id_people, db, PeoplesModel, CarsModel)
    if isNotValidJson:
        return isNotValidJson

    return CreateCar.create()


@app.route("/register", methods=["POST"])
# @token_required
# deixei rota aberta só por questões de homologação
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
