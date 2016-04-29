# gfxsked
Graphics Request Scheduler System


### INTRODUCTION
-------------

Objective: to create an internal tool to manage, schedule, and assign requests regarding any graphics project.
GFXSKED currently stores both types of request, an idea requests or a detailed request, into one database.


### REQUIREMENTS
------------

GFXSKED requires Django version 1.9 or higher. 
See Requirements.txt for more info. 


### INSTALLATION
------------

1. Download Django 1.9.2
```sh
pip install Django==1.9.2
```

2. Download GFXSKED source code. 

3. Run application. 


### RUNNING APPLICATION
-------------------

1. Go into the file where manage.py is stored.
Change into /gfsked directory or where manage.py is stored.
```sh
 cd /gfxsked
```

2. run application with the following command.

```sh
python manage.py runserver
```

You should see a similar output. 
```sh
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

April 29, 2016 - 15:50:53
Django version 1.9, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

3. Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser. 

### RUNNING TESTS
-------------

Store all tests under tests.py. 
View Django's documentation on testing here. https://docs.djangoproject.com/en/1.9/topics/testing/overview/


### KNOWN BUGS
---------

- Log In button directs to log out page
- Data files aren't stored for requests


### DJANGO HELP
-----------

View Django support and documentation on Django's site. https://docs.djangoproject.com/en/1.9/