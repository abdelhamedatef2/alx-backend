# 0x02-i18n
![91e1c50322b2428428f9](https://github.com/abdelhamedatef2/alx-backend/assets/118136210/873de28f-1dca-449f-9894-a6f0bd2f3f33)

### Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- The first line of all your files should be exactly #!/usr/bin/env python3
- All your *.py files should be executable
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions and methods should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

### Tasks

#### 0-app.py
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).

#### 1-app.py
Install the Babel Flask extension:
```
$ pip3 install flask_babel==2.0.0
```
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.
In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en") and timezone ("UTC").
Use that class as config for your Flask app.

#### 2-app.py
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.

#### 3-app.py, babel.cfg
Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.
Create a babel.cfg file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```
Then initialize your translations with
```
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:
```
msgid	English	French
home_title	"Welcome to Holberton"	"Bienvenue chez Holberton"
home_header	"Hello world!"	"Bonjour monde!"
```
Then compile your dictionaries with
```
$ pybabel compile -d translations
```
Reload the home page of your app and make sure that the correct messages show up.

#### 4-app.py
n this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.
In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.
Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].
Visiting http://127.0.0.1:5000/?locale=fr should display this level 1 heading:

#### 5-app.py
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.
```
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.
Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.
Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

#### 6-app.py
Change your get_locale function to use a user’s preferred local if it is supported.
The order of priority should be
1- Locale from URL parameters
2- Locale from user settings
3- Locale from request header
4- Default locale
Test by logging in as different users

#### 7-app.py
Define a get_timezone function and use the babel.timezoneselector decorator.
The logic should be the same as get_locale:
1- Find timezone parameter in URL parameters
2- Find time zone from user settings
3- Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.
