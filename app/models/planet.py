from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    order = db.Column(db.Integer)
    # __tablename__ = "books"# optional: w/out this, it will just link the model to a table with the exact asme name as the class Book, not


    def to_string(self):
        return f"{self.id}: {self.name} Description: {self.description}"