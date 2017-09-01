from hmc.database import db, Column, String

class User(db.Model):
    username = Column(String(20), primary_key=True)
    nickname = Column(String(30))
    password_md5 = Column(String(50))