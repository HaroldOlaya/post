from flask import Flask, render_template, request,redirect,url_for
import db
from models import Tarea
app=Flask(__name__) # en app se encuentra nuestro servidor web flask


@app.route("/")
def home():
    todas_las_tareas=db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    return render_template("index.html",lista_tareas=todas_las_tareas)

@app.route("/crear-tarea",methods=["POST"] )
def crear():
    tarea=Tarea(contenido=request.form["contenido_tarea"],hecho=False) #request es lo que nos permite sacar la informacion del html index
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>" )
def eliminar(id):
    tarea=db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/hecha-tarea/<id>" )
def hecha(id):
    tarea=db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecho = not (tarea.hecho)
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return render_template("logrado.html")

if __name__=="__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
