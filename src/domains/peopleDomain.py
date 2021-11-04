class PeopleDomain:
    def create(data, db, PeoplesModel):
        objectDB = PeoplesModel(**data)
        db.session.add(objectDB)
        db.session.commit()
        return data

    def update_sale_opportunity(db, id, PeoplesModel):
        people = PeoplesModel.query.filter(PeoplesModel.id == id).first()
        people.sale_opportunity = False
        db.session.add(people)
        db.session.commit()

    def id_is_valid(db, id, PeoplesModel):
        return PeoplesModel.query.filter(PeoplesModel.id == id).first()

    def cars_by_people(db, id, PeoplesModel):
        cars = PeoplesModel.query.filter(
            PeoplesModel.id == id).first().peoples_cars_relationship
        if len(cars) >= 3:
            return True
        return False
