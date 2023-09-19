from app import app, db


class Receipts(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    retailer = db.Column(db.String)
    purchaseDate = db.Column(db.String)
    purchaseTime = db.Column(db.String)
    total = db.Column(db.String)
    items = db.Relationship('Items', backref='receipts', lazy='dynamic')


class Items(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    shortDescription = db.Column(db.String)
    price = db.Column(db.String)
    receipt = db.Column(db.Integer, db.ForeignKey('receipts.id'))


with app.app_context():
    db.create_all()
