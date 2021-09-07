import requests
from .config import *
import datetime



def get_repositories(params):
    response = requests.get(BASEURL, params=params)
    if response.ok:
        return response.json()
    return None
    



