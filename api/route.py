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
    # if the user wants to get trending langauges used from a spesific date
    start_date = request.args.get('start_date')
    # default start date is 30 days ago from todays date
    if start_date is None:
        date = datetime.datetime.now() - datetime.timedelta(30)
        start_date = str(date.date())
    # github endpoint paramters
    params = params = dict(q=f"created:>{start_date}", sort='stars', order='desc', per_page=100)
    # get the response repositories from github
    repositories = get_repositories(params=params)
    # where we store the api response
    data = {}
    # to locate the trend language 
    trend_lang = [0, ""]
    # to compute number if repositories that has no spesific language
    n_nones = 0
    # check if we got a success response 200
    if repositories:
        # for each repository in the response
        for item in repositories["items"]:
            # get the language used in it
            lang = str(item['language']).lower()
            # create a Repository object with the needed information
            repos_info = Repository(full_name=item['full_name'], url=item['url'])
            # check if language not none
            if lang != "none":
                # check if already added this language to our data
                if lang in data.keys():
                    # add it to the data and augment the count
                    data[lang].count += 1
                    data[lang].repositories.append(repos_info)
                    # check if it's count is the highest update the trend_language
                    if trend_lang[0] < data[lang].count:
                        trend_lang[0] = data[lang].count
                        trend_lang[1] = data[lang].name
                else:
                    # if we haven't add this language create the Language object and add the informations
                    data[lang] = Language(name=lang, count=1, repositories=[repos_info])
            else:
                # in case we got a none augment the number
                n_nones += 1

        # return the result data
        return {
            "trend_language":{"name":trend_lang[1], "count":trend_lang[0]},
            "n_none_language":n_nones,
            "start_date": start_date,
            "items": [LanguageSchema().dump(item) for item in data.values()]
        }
    # in case we got a bad response
    return None
                
