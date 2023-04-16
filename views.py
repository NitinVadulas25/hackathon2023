from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def asfhjasfh():
    return render_template("home.html")


@views.route('/goober', methods=["GET", "POST"])
def hfhs():
    return render_template("base2.html")