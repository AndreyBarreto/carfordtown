

class CarDomain:
    def create(data, db, CarsModel):
        try:
            objectDB = CarsModel(**data)
            db.session.add(objectDB)
            db.session.commit()
            return data
        except Exception as e:
            return ""
