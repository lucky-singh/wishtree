from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Feature(db.Model):
    __tablename__ = "features"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    client = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    targetDate = db.Column(db.Date, nullable=False)
    productArea = db.Column(db.String, nullable=False)



class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String, nullable=False)


class ProductArea(db.Model):
    __tablename__ = "productAreas"
    id = db.Column(db.Integer, primary_key=True)
    productArea = db.Column(db.String, nullable=False)


def main():
    pass


if __name__ == "__main__":
    main()
