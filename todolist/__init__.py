from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = 'e80bc3ecc92b94c00c37626bcfd40bd0'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///accounts.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db=SQLAlchemy(app)
migrate = Migrate(app, db)
from todolist import views
from todolist import models
if __name__ == "__main__":
    app.run(debug=False)



