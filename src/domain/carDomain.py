from logging import error


class CarDomain:
    def create(data, id_person, db, PeopleModel, CarsModel):
        try:
            objectDB = CarsModel(**data)
            db.session.add(objectDB)
            db.session.commit()
            return data
        except Exception as e:
            return ""
