from flask import Flask,redirect, render_template
from flask import url_for
from flask import request
import forms

from flask import jsonify
from config import Developmentconfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(Developmentconfig)
csrf=CSRFProtect()

@app.route("/")
def index():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nombre=create_form.nombre.data,
                     apellidos=create_form.apellidos.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.comit()
    return render_template('index.html',form=create_form)
    
@app.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_form=forms.UserForm(request.form)
     #select *from alumnos where id==id
    Alumnos=Alumnos.usery.all()

@app.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #select *from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.email
        
    if request.method=='POST':
        id=request.args.get('id')
         #select *from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nombre=create_form.nombre.data
        alum1.apellidos=create_form.apellidos.data
        alum1.email=create_form.email.data
        db.session.add(alum1)
        db.session

if __name__=='__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)