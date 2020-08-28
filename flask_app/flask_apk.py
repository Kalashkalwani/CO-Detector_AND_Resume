from flask import render_template, Flask,request
from flask_sqlalchemy import SQLAlchemy
import mytraining as mt
import datetime



local_server = True
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Kalashkalwani:harsh@03@kalashkalwani.mysql.pythonanywhere-services.com/Kalashkalwani$kalwani_codex'

db = SQLAlchemy(app)


class Contact(db.Model):
    '''ADDING ELEMENT TO DATABASE'''

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(13), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),default=datetime.datetime.now())
    email = db.Column(db.String(20))

class Collaborate(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12), default=datetime.datetime.now())
    email = db.Column(db.String(20))


@app.route('/',methods={"POST","GET"})
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, email=email, phone_num=phone, msg=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("index.html")


@app.route("/CODetector",methods=['GET','POST'])
def CODetector():
    mydict = request.form

    if request.method == 'POST' and not len(mydict) == 1:
        fever = int(mydict['fever'])
        bodypain = int(mydict['bodypain'])
        age = int(mydict['Age'])
        runnynose = int(mydict['runnynose'])
        diffBreadth = int(mydict['diffBreath'])

        inputfeature = [fever, bodypain, age, runnynose, diffBreadth]
        infprob = mt.model(inputfeature)
        return render_template("show.html", inf=round(infprob * 100))

    if request.method == 'POST' and len(mydict) == 1:
        email = request.form.get('email')
        entry = Collaborate(email=email, date=datetime.datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template("co.html")


