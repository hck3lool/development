from flask import Flask, render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///data.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20), nullable = False)
    edad = db.Column(db.Integer, nullable = False) 
    sexo = db.Column(db.String(1), nullable = False)
    nacionalidad = db.Column(db.String(20), nullable = False)
    provincia = db.Column(db.String(20), nullable = False)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)

    def __resp__(self):
        return '<Datos %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
       nombre_registrado = request.form['nombre'] 
       edad_registrada = request.form['edad']
       sexo_registrado = request.form['sexo']
       nacionalidad_registrada = request.form['nacionalidad']
       provincia_registrada = request.form['provincia']
       nuevo_registro = Todo(nombre = nombre_registrado, edad = edad_registrada, sexo = sexo_registrado, 
       nacionalidad = nacionalidad_registrada, provincia = provincia_registrada)
       try:
           db.session.add(nuevo_registro)
           db.session.commit()
           return redirect('/')
       except:
            return "Ocurrio un problema al agregar la tarea"
    else:
        datos = Todo.query.order_by(Todo.fecha).all()
        return render_template('index.html', datos = datos)

@app.route('/borrar/<int:id>')
def borrar(id):
    tarea_a_eliminar = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(tarea_a_eliminar)
        db.session.commit()
        return redirect('/')
    except:
        return "Ocurrio un problema al eliminar los datos"

@app.route('/actualizar/<int:id>',methods=['POST','GET'])
def actualizar(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.nombre = request.form['nombre']
        task.edad = request.form['edad']
        task.sexo = request.form['sexo']
        task.nacionalidad = request.form['nacionalidad']
        task.provincia = request.form['provincia']
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "Ocurrio un problema al actualizar los datos"

    else:
        return render_template("update.html", task = task)
    
if __name__ == "__main__":
    app.run(debug=True)
