

class UserDomain:
    def create(data, db, UsersModel):
        try:
            objectDB = UsersModel(**data)
            db.session.add(objectDB)
            db.session.commit()
            return {"success": "User Created"}
        except Exception as e:
            return ""

    def find(data, db, UsersModel):
        return UsersModel.query.filter(
            UsersModel.username == data["username"]).first()
