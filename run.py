from flask import Flask, render_template

app = Flask(__name__, template_folder="webapp/templates")

users = [
    {'id': 1, 'name': 'Alan'},
    {'id': 2, 'name': 'Alice'},
    {'id': 3, 'name': 'Phil'}
]


@app.route("/home")
@app.route("/")
def hello():
    return render_template("index.html", title="Hello DIA")


@app.route("/category")
def category():
    return "<p>Hello Category</p>"


@app.route("/users")
def users_list():
    return render_template("users.html", title="Liste des utilisateurs", users=users)
