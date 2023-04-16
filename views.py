from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def asfhjasfh():
    return render_template("home.html")


@views.route('/volunteer', methods=["GET", "POST"])
def hfhs():
    return render_template("volunteer.html")


@views.route('/create-volunteer', methods=["GET", "POST"])
def jack():
    return render_template("create-volunteer.html")
