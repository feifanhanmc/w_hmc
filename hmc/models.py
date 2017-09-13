from hmc.database import db

class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    nickname = db.Column(db.String(30))
    password_md5 = db.Column(db.String(50))
    def __repr__(self):
        return "<User(username='%s', nickname='%s')>" % ( self.username, self.nickname)

class BDUser(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    nickname = db.Column(db.String(30))
    comname = db.Column(db.String(30))
    password_md5 = db.Column(db.String(50))
    def __repr__(self):
        return "<User(username='%s', nickname='%s')>" % ( self.username, self.nickname)

class BDRecord(db.Model):
    record_id = db.Column(db.String(50), primary_key=True)
    bd_username = db.Column(db.String(20))
    merchant_name = db.Column(db.String(50))
    merchant_tel = db.Column(db.String(20))
    visit_purpose = db.Column(db.String(30))
    visit_result = db.Column(db.String(100))
    visit_time = db.Column(db.String(20))
