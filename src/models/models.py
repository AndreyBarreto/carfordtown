class Models:
    def generate(db):
        class Peoples(db.Model):
            __tablename__ = 'peoples'
            id = db.Column(db.BigInteger, primary_key=True)
            name = db.Column(db.String())
            sale_opportunity = db.Column(db.Boolean, default=1)

            peoples_cars_relationship = db.relationship(
                "Cars",
                primaryjoin="Peoples.id == Cars.id_people"
            )

        class Cars(db.Model):
            __tablename__ = 'cars'
            id = db.Column(db.BigInteger, primary_key=True)
            model = db.Column(db.String())
            color = db.Column(db.String())
            id_people = db.Column(db.Integer(), db.ForeignKey("peoples.id"))

        class User(db.Model):
            __tablename__ = 'users'
            id = db.Column(db.BigInteger, primary_key=True)
            username = db.Column(db.String())
            password = db.Column(db.String())

        db.create_all()

        return (Peoples, Cars, User)
