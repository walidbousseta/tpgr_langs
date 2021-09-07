from flask import Blueprint


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
    return {"message":"welcome to the api!"}


