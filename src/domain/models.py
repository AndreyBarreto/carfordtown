class Models:
    def generate(db):
        class Person(db.Model):
            __tablename__ = 'person'
            id = db.Column(db.BigInteger, primary_key=True)
            name = db.Column(db.String())
            sale_opportunity = db.Column(db.Boolean, default=1)

            person_cars_relationship = db.relationship(
                "Cars",
                primaryjoin="Person.id == Cars.id_people"
            )

        class Cars(db.Model):
            __tablename__ = 'cars'
            id = db.Column(db.BigInteger, primary_key=True)
            model = db.Column(db.String())
            color = db.Column(db.String())
            id_people = db.Column(db.Integer(), db.ForeignKey("person.id"))

        db.create_all()

        return (Person, Cars)
