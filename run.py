
from flask import render_template,url_for,redirect,request,flash
from _forms import Register
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET KEY'] = 'Tma*@1111'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///user.db'

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'f9ec9f35fbf2a9d8b95f9bffd18ba9a1'

_form = []


class User(db.Model):

    #Create Columns
    id = db.Column(db.Integer,primary_key=True)
    name = db.db.Column(db.String(20),unique=True)
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(120), unique=True)
    confirm_password = db.Column(db.String(120), unique=True)

    # def __init__(self,name,email,password,confirm_password,id=None):
    #
    #     self.id = id
    #     self.name = name
    #     self.email=email
    #     self.password = password
    #     self.confirm_password = confirm_password


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sign_up", methods=["POST","GET"])
def sign_up():
    # from myproject.models import user
    register = Register()
    # db.init_app(app)
    if request.method == "POST":
        #append to _form list, to handle it on backend
        if register.validate_on_submit() == False:
            print("Yes Valid")
            flash(f'Hey {register.name.data} You Have Successfully Registered','success')
            print(register.name.data,register.email.data,register.password.data,register.confirm.data)
            user1 = User(name=register.name.data,email=register.email.data,password=register.password.data,confirm_password=register.confirm.data)
            db.session.add(user1)
            print("----Ran Second ---")
            db.session.commit()

            return redirect(url_for('home'))

        else:
            print(register.validate_on_submit())
            print(register.name.data, register.email.data, register.password.data, register.confirm.data)
            print('Error Confirm: ', register.confirm.errors)
            print('Error Confirm: ', register.email.errors)
            print('Error Confirm: ', register.password.errors)
            print('Error Confirm: ', register.name.errors)
            return redirect(url_for('sign_up'))#render_template("sign_up_form.html", register=register)



    else:
        return render_template("sign_up_form.html",register=register)


@app.route("/create")
def create():
    db.create_all()
    return f'"All Tables"'


@app.route("/user")
def user():

    ser1 = User().query.all()
    print(ser1[0])

    return f"{ser1[0]}"

@app.route("/retrieve")
def retrieve():
    name = "/home/aspire/PycharmProjects/myproject/Instance/user"
    print(Retrieve_db(db_name=name).get_users())
    return f"{Retrieve_db(db_name=name).get_users()}"




if __name__ == "__main__":

    app.run(debug=True)


