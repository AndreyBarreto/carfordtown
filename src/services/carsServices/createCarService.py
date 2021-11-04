from domain.carDomain import CarDomain
from domain.peopleDomain import PeopleDomain
from jsonschema import validate


class createCarService:
    def validate(self, data):
        schema = {
            "type": "object",
            "required": ["color", "model"],
            "properties": {
                "color": {
                    "type": "string",
                    "enum": ["yellow", "blue", "gray"]
                },
                "model": {
                    "type": "string",
                    "enum": ["hatch", "sedan", "convertible"]
                }
            },
            "additionalProperties": False
        }

        try:
            validate(data, schema)
        except Exception as e:
            return {"error": e.message}, 400

    def create(self, data, id_people, db, PeopleModel, CarsModel):
        data["id_people"] = id_people

        peopleExist = PeopleDomain.id_is_valid(db, id_people, PeopleModel)
        if not peopleExist:
            return {"error": "ID for people not found"}, 400

        moreThanThreeCars = PeopleDomain.cars_by_people(
            db, id_people, PeopleModel)
        if moreThanThreeCars:
            return {"error": f"People ID {id_people} already have 3 cars"}, 400

        carCreated = CarDomain.create(
            data, id_people, db, PeopleModel, CarsModel)
        if carCreated:
            people = PeopleDomain.update_sale_opportunity(
                db, id_people, PeopleModel)
            return data
        return {"error": "Car needs a valid id people"}, 400