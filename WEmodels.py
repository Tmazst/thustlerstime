from myproject.run import db

#Users class, The class table name 'h1t_users_cvs'
class user(db.Model):

    #Create Columns
    id = db.Column(db.Integer,primary_key=True)
    name = db.db.Column(db.String(20),unique=True)
    # username = db.Column(db.String(20),unique=True)     #Username, we want it to be unique, nullable
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(120), unique=True)
    confirm_password = db.Column(db.String(120), unique=True)

    # def __init__(self,id,name,email,password,confirm_password):
    #     self.id = id
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.confirm_password = confirm_password




