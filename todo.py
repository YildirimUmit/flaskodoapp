from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/UMYLD/Desktop/TODOAPP/todo.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    todos=todu.query.all()


    return render_template("index.html",todos=todos)

@app.route("/complete/<string:id>")
def completeTodo(id):
    todu1 =todu.query.filter_by(id = id).first()
    todu1.complete=not todu1.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delet(id):
     todu1 =todu.query.filter_by(id = id).first()
     db.session.delete(todu1)
     db.session.commit()
     return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def addTodu():
    title=request.form.get("title")
    newTodo=todu(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))


class todu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean)

if  __name__=="__main__":
    db.create_all()
    app.run(debug=True)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username