from domains.peopleDomain import PeopleDomain
from jsonschema import validate


class createPersonService:
    def validate(self, data, db, PeoplesModel):
        self.data = data
        self.db = db
        self.PeoplesModel = PeoplesModel

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

    def create(self):
        return PeopleDomain.create(self.data, self.db, self.PeoplesModel)
