from flask import Flask

def createapp():
    app = Flask(__name__)
    from views import views
    app.register_blueprint(views, url_prefix = '/')
    return app

app = createapp()

if __name__ == "__main__":
    app.run(debug=False)