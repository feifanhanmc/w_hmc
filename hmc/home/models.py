from hmc.database import db#, Column, String

class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    nickname = db.Column(db.String(30))
    password_md5 = db.Column(db.String(50))
    def __repr__(self):
        return "<User(username='%s', nickname='%s')>" % ( self.username, self.nickname)