from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")

@views.route('/volunteer', methods=["GET", "POST"])
def volunteer():
    return render_template("volunteer.html")

@views.route('/contributions', methods=["GET", "POST"])
def reducer():
    return render_template("reducer.html")
