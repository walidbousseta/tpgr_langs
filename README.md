# TPGR_Langs
REST microservice that list the languages used by the 100 trending public repos on GitHub.

## Dependencies
certifi==2021.5.30
charset-normalizer==2.0.4
click==8.0.1
colorama==0.4.4
Flask==2.0.1
flask-marshmallow==0.14.0
idna==3.2
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
marshmallow==3.13.0
requests==2.26.0
six==1.16.0
urllib3==1.26.6
Werkzeug==2.0.1

## How to run
1. activate the environment by `.\env\Scripts\activate`
2. install the requirements by `pip install -r requirements.txt`
3. set the falsk app
  - for windows use `set FLASK_APP=app.py`
  - for lunix use `export FLASK_APP=run.py`
4. run the server using `flask run`

## Api endpoints
**/languages**: 
to get languages used by the 100 trending repositories

params:
* _start_date_: from which date to start counting to get the trend languages (default 30 days ago from todays date)

response :
```json
{
 "items": [
        {
          "count": 10,
          "name": "javascript",
          "repositories": [
            {
              "full_name": "xxx xxxx xxxxxx",
              "url": "https://api.github.com/repos/xxxxxxx/xxxxxxx"
            },
            {
              "full_name": "xxx xxxx xxxxxx",
              "url": "https://api.github.com/repos/xxxxxxx/xxxxxxx"
            },
          ]
        },
        {
          "count": 20,
          "name": "python",
          "repositories": []
        },
        ],
 "n_none_language": 17,
 "start_date": "2021-08-09",
 "trend_language": {
          "count": 20,
          "name": "python"
        }
}
```





