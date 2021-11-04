from domain.peopleDomain import PeopleDomain
from jsonschema import validate


class createPersonService:
    def validate(self, data):
        schema = {
            "type": "object",
            "required": ["name"],
            "properties": {
                "name": {
                    "type": "string"
                }
            },
            "additionalProperties": False
        }

        try:
            validate(data, schema)
        except Exception as e:
            return {"error": e.message}, 400

    def create(self, data, db, PeopleModel):
        return PeopleDomain.create(data, db, PeopleModel)
