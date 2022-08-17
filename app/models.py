from app import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    phone_number = db.Column(db.String(15), nullable = False, unique = True)
    address = db.Column(db.String(100), nullable = False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Address | {self.name}>'

    def __str__(self):
        return f'''
        Name: {self.name}
        Phone Number: {self.phone_number}
        Address: {self.address}
        '''