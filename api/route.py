from flask import Blueprint, request
from .service import *
from .model import *
from .schema import *


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/')
def index():
    return {"message":"welcome to the api!"}


@api.route('/repositories', methods=["GET"])
def repositories():
    start_date = request.args.get('start_date')
    if start_date is None:
        date = datetime.datetime.now() - datetime.timedelta(30)
        start_date = str(date.date())
    params = params = dict(q=f"created:>{start_date}", sort='stars', order='desc', per_page=100)
    repositories = get_repositories(params=params)
    data = {}
    if repositories:
        for item in repositories["items"]:
            lang = str(item['language'])
            repos_info = Repository(full_name=item['full_name'], url=item['url'])
            if lang in data.keys():
                data[lang].count += 1
                data[lang].repositories.append(repos_info)
            else:
                data[lang] = Language(name=lang, count=1, repositories=[repos_info])

        return {"items": [LanguageSchema().dump(item) for item in data.values()]}
    
    return None
                
