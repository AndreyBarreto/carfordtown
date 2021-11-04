class PeopleDomain:
    def create(data, db, PeopleModel):
        objectDB = PeopleModel(**data)
        db.session.add(objectDB)
        db.session.commit()
        return data

    def update_sale_opportunity(db, id, PeopleModel):
        people = PeopleModel.query.filter(PeopleModel.id == id).first()
        people.sale_opportunity = False
        db.session.add(people)
        db.session.commit()

    def id_is_valid(db, id, PeopleModel):
        return PeopleModel.query.filter(PeopleModel.id == id).first()

    def cars_by_people(db, id, PeopleModel):
        cars = PeopleModel.query.filter(
            PeopleModel.id == id).first().person_cars_relationship
        if len(cars) >= 3:
            return True
        return False
