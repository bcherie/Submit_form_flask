from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)


@app.route("/success")
def success():
    return render_template("successful.html", title="Страница success")



@app.route("/", methods=("POST", "GET"))
@app.route("/form", methods=("POST", "GET"))
def form():
    if request.method == "POST":
        try:
            email = request.form["email"]
            name = request.form["name"]
            user = Users(name=name, email=email)
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            print("Error enter")

        return redirect(url_for('success'))

    return render_template("form.html", title="Форма заявки")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)