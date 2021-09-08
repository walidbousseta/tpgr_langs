from flask import Blueprint, request
from .service import *
from .model import *
from .schema import *

# define the api route application
api = Blueprint('api', __name__, url_prefix='/api')

# index page of the api
@api.route('/')
def index():
    return {"message":"welcome to the api!"}

# to get languages
@api.route('/languages', methods=["GET"])
def languages():
    start_date = request.args.get('start_date')
    if start_date is None:
        date = datetime.datetime.now() - datetime.timedelta(30)
        start_date = str(date.date())
    params = params = dict(q=f"created:>{start_date}", sort='stars', order='desc', per_page=100)
    repositories = get_repositories(params=params)
    data = {}
    trend_lang = [0, ""]
    n_nones = 0
    if repositories:
        for item in repositories["items"]:
            lang = str(item['language']).lower()
            repos_info = Repository(full_name=item['full_name'], url=item['url'])
            if lang != "none":
                if lang in data.keys():
                    data[lang].count += 1
                    data[lang].repositories.append(repos_info)
                    if trend_lang[0] < data[lang].count:
                        trend_lang[0] = data[lang].count
                        trend_lang[1] = data[lang].name
                else:
                    data[lang] = Language(name=lang, count=1, repositories=[repos_info])
            else:
                n_nones += 1

        return {
            "trend_language":{"name":trend_lang[1], "count":trend_lang[0]},
            "n_none_language":n_nones,
            "start_date": start_date,
            "items": [LanguageSchema().dump(item) for item in data.values()]
        }
    
    return None
                
