from flask import Flask

def create_app(): 
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jaydogg131@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from . import models
    models.db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return '<a href="/pets"> Hello, PetFax!</a>'
   
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    
    return app

