from domains.carDomain import CarDomain
from domains.peopleDomain import PeopleDomain
from jsonschema import validate


class createCarService:
    def validate(self, data, id_people, db, PeoplesModel, CarsModel):
        self.data = data
        self.id_people = id_people
        self.db = db
        self.PeoplesModel = PeoplesModel
        self.CarsModel = CarsModel

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

    def create(self):
        self.data["id_people"] = self.id_people

        peopleExist = PeopleDomain.id_is_valid(
            self.db, self.id_people, self.PeoplesModel)
        if not peopleExist:
            return {"error": "ID for people not found"}, 400

        moreThanThreeCars = PeopleDomain.cars_by_people(
            self.db, self.id_people, self.PeoplesModel)
        if moreThanThreeCars:
            return {"error": f"People ID {self.id_people} already have 3 cars"}, 400

        carCreated = CarDomain.create(
            self.data, self.db,  self.CarsModel)
        if carCreated:
            PeopleDomain.update_sale_opportunity(
                self. db, self.id_people, self.PeoplesModel)
            return self.data
        return {"error": "Car needs a valid id people"}, 400
