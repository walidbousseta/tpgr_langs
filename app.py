from flask import Flask
from .config import *

from .site.route import site
from .api.route import api



def create_app():
    app = Flask(__name__)
    app.register_blueprint(site)
    app.register_blueprint(api)
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host=HOST, port=PORT)




