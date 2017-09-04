# UrlShortener

###### Repository which provides an API to generate short urls.

Project codebase: <https://github.com/omprakash1989/UrlShortener>

***
#### Git Local Config

`git config --global user.name "<First-Name> <Last-Name>"`

`git config --global user.email "<youremailaddress>"`

#### Python Library Requirements

All the python library requirements are specified in requirements.txt file.

To install the required libraries:

- `pip install -r requirements.txt`


(PS: Linux/Mac Users can use virtualenv. Refer to [DOC] [venv-doc])


Installing MysqlServer for safer side (OS dependent) else MySQL-python package will do fine.

`sudo aptitude install mysql-server-5.6 libmysqlclient-dev`


Create DB and DB User.

`CREATE DATABASE url_shortener CHARACTER SET utf8 COLLATE utf8_unicode_ci;`

`create user 'livelike'@'localhost' identified by 'livelike';`

`grant all on url_shortener.* to 'livelike'@'localhost';`


Initial migrations:

- `python manage.py migrate`


Create Superuser:

- `python manage.py createsuperuser`


Getting ACCESS TOKEN from provider:


- Register on [Bitly] [bitly-home]

- Go to [Manage Apps] [bitly-manage-apps]

- generate token by verifying.

- Go to settings file of the application at path `UrlShortner/settings.py` and paste the fetched ACCESS TOKEN against variable `API_ACCESS_TOKEN`


### Focused on

- API to create short url.

- Saved to a model to restrict redudant API calls to short url provider which is advised to be managed according to requirements (like when to expire and regenerate.).


### APIS
--------

##### to create a short url from given long url:

`/api/v1/shortner/get-short-url/`


### Running Application
-----------------------

- Move to backend application: `cd UrlShortener/`

- Activate virtual environment if required.

- Running Server: `python manage.py runserver`

- Tests: `python manage.py test notifications.tests (Server should be running)`


### Stacks Used
---------------
- Python

- Django

- MySql


### References Taken
--------------------
Bitly [Developer API Documentation] [dev-api-doc]


[URL Shortening Wiki] [url-shortening-wiki]



[venv-doc]: 'http://docs.python-guide.org/en/latest/dev/virtualenvs/'
[bitly-home]: 'https://bitly.com/'
[bitly-manage-apps]: 'https://bitly.com/a/oauth_apps'
[dev-api-doc]: 'https://dev.bitly.com/api.html'
[url-shortening-wiki]: 'https://en.wikipedia.org/wiki/URL_shortening'
