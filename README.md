# Cookiecutter skeleton for Minimal Flask application


## Requirements

- python (Tested on 3.6.6 . For 2.x.x, requirements and some 'import' could be changed)
- cookiecutter (Install it using `pip install cookiecutter`)


## Usage

### Method 1 using remote url

    > cookiecutter git@github.com:rohitchormale/cookiecutter-flask-minimal.git
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty, 'myproject' will be created in current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


### Method 2 from source

    > git clone git@github.com:rohitchormale/cookiecutter-flask-minimal.git
    > cookiecutter <absolute-path-to-cloned-repo>
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


## Skeleton structure


    myproject
    ├── config.py
    ├── instance
    │   └── config.py
    ├── myproject
    │   ├── commands.py
    │   ├── controllers.py
    │   ├── extensions.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── routes.py
    │   └── ui
    │       ├── static
    │       │   ├── css
    │       │   │   └── styles.css
    │       │   └── js
    │       │       └── custom.js
    │       └── templates
    │           └── index.html
    ├── README.md
    ├── requirements.txt
    └── wsgi.py



* **myproject/myproject/__init__.py** - Your project starts here. Blueprints, extensions, commands and all other fancy stuff
will be defined in their own modules. But all those components will be hooked up together here. 
See [application-factories](http://flask.pocoo.org/docs/1.0/patterns/appfactories/).
 
* **myproject/myproject/routes.py** - These are your URLs grouped together using [blueprints](http://flask.pocoo.org/docs/1.0/blueprints/).
They are pointed to controllers.
* **myproject/myproject/controllers.py** - Define your controllers here to manipulate views and database. Similar to `views.py` in django.
So flow will be `url-> controller -> template/database`.
* **myproject/myproject/extensions.py** - Instantiate flask extensions here so those can be easily accessed in other modules.
Extensions can be initialized in `myproject/myproject/__init__.py` also. Keeping them separate, will look clean. Important point is,
after you INSTANTIATE extension here, you need to INITIATE it again in `myproject/myproject/__init__.py/create_app`. 
You can see example format in comments once app is created.
* **myproject/myproject/forms.py** - Create your http forms here. See [wtforms](http://flask.pocoo.org/docs/1.0/patterns/wtforms/) 
* **myproject/myproject/models.py** - Create your database models here. See [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/).
Make sure to enable related extension for this. Database url will be configured in configuration files. See below.
* **myproject/myproject/commands.py** - Custom terminal commands to ease your workflow. See [flask-cli](http://flask.pocoo.org/docs/1.0/cli/)

* **myproject/myproject/ui/static** - keep your static files like css, js, media here.
* **myproject/myproject/ui/templates** - keep your http templates here.

* **myproject/README.md** - Information about project.
* **myproject/requirements.txt** - Python modules used in project.
* **myproject/wsgi.py** - `wsgi` module to integrate app with web servers like apache, gunicorn. See [mod_wsgi](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/).
* **myproject/config.py** - Project permanent configuration. This should be committed in version control tool. Similar to `settings.py` in django.
* **myproject/instance/config.py** - Project temporary config like secrets etc. It MUST NOT be committed in version control tool. 



## Bootstrapping

By default, development environment is not enabled. To enable it, set environmental variable 'FLASK_ENV=development'.
Development server can be started using `flask run` command. While to integrate your app with web servers like apache,
use `wsgi.py` module, mentioned above.


## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
- [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [FLask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
