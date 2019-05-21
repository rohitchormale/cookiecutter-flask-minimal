# Cookiecutter skeleton for Minimal Flask application


## Requirements

- python (Tested on 3.6.6 . For 2.x.x, requirements and some 'import' could be changed)
- cookiecutter (Install it using `pip install cookiecutter`)


## Usage

### Method 1 using remote url

    > cookiecutter https://github.com/rohitchormale/cookiecutter-flask-minimal.git
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty, 'myproject' will be created in current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


### Method 2 from source

    > git clone https://github.com/rohitchormale/cookiecutter-flask-minimal.git
    > cookiecutter <absolute-path-to-cloned-repo>
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


## Skeleton structure


    myproject
    │
    ├── myproject
    │   ├── __init__.py
    │   ├── extensions.py
    │   ├── routes.py
    │   ├── controllers.py
    │   ├── models.py
    │   ├── forms.py
    │   ├── commands.py
    │   │
    │   └── ui
    │       ├── static
    │       │   ├── css
    │       │   │   └── styles.css
    │       │   └── js
    │       │       └── custom.js
    │       └── templates
    │           └── index.html
    │
    ├── tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── test_controllers.py
    │
    ├── config.py
    ├── instance
    │   └── config.py
    ├── wsgi.py
    │
    ├── requirements.txt
    └── README.md



* **myproject/myproject/__init__.py** - Your project starts here. Blueprints, extensions, commands and all other fancy stuff
will be defined in their own modules. But all those components will be hooked up together here. 
See [application-factories](http://flask.pocoo.org/docs/1.0/patterns/appfactories/).
* **myproject/myproject/extensions.py** - Instantiate flask extensions here so those can be easily accessed in other modules.
Extensions can be initialized in `myproject/myproject/__init__.py` also. Keeping them separate, will look clean. Important point is,
after you INSTANTIATE extension here, you need to INITIATE it again in `myproject/myproject/__init__.py/create_app`. 
You can see example format in comments once app is created.

* **myproject/myproject/routes.py** - These are your URLs grouped together using [blueprints](http://flask.pocoo.org/docs/1.0/blueprints/).
They are pointed to controllers.
* **myproject/myproject/controllers.py** - Define your controllers here to manipulate views and database. Similar to `views.py` in django.
So flow will be `url-> controller -> template/database`.
* **myproject/myproject/forms.py** - Create your http forms here. See [wtforms](http://flask.pocoo.org/docs/1.0/patterns/wtforms/) 
* **myproject/myproject/models.py** - Create your database models here. See [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/).
Make sure to enable related extension for this. Database url will be configured in configuration files. See below.
* **myproject/myproject/commands.py** - Custom terminal commands to ease your workflow. See [flask-cli](http://flask.pocoo.org/docs/1.0/cli/)

* **myproject/myproject/ui/static** - keep your static files like css, js, media here.
* **myproject/myproject/ui/templates** - keep your http templates here.

* **tests/conftest.py** - Test support is added using [pytest](https://docs.pytest.org/en/latest/). Common config/fixtures and plugin-loadings can be done in this module.
* **tests/test_controllers.py** - Add unit testcases in this module. 

* **myproject/config.py** - Project permanent configuration. This should be committed in version control tool. Similar to `settings.py` in django.
* **myproject/instance/config.py** - Project temporary config like secrets etc. It MUST NOT be committed in version control tool. 
* **myproject/wsgi.py** - `wsgi` module to integrate app with web servers like apache, gunicorn. See [mod_wsgi](http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/).

* **myproject/requirements.txt** - Python modules used in project.
* **myproject/README.md** - Information about project.


## Bootstrapping

By default, development environment is not enabled. To enable it, set environmental variable 'FLASK_ENV=development'.
Development server can be started using `flask run` command. While to integrate your app with web servers like apache,
use `wsgi.py` module, mentioned above.


## Testing


### Testing using pytest

By default this skeleton supports [pytest](https://docs.pytest.org/en/latest/) using its flask-extension [pytest-flask](http://pytest-flask.readthedocs.org/en/latest/).
Run pytest-flask using command `pip install pytest-flask`.  Run test cases using below commands. See pytest docs for more info.


    # To run all testcases
    pytest tests
    
    # To disable warnings
    pytest --disable-warnings tests
    
    # To replace sys.stdout/stderr with in-mem files 
    pytest --disable-warnings --capture=sys
    
    # RUn test cases from specific module
    pytest --disable-warnings tests/test_controllers.py --capture=sys
    
    # Run specific testsuit from given module
    pytest --disable-warnings tests/test_controllers.py  -k 'TestUser' --capture=sys
    
    # Run specific testcase from given module
    pytest --disable-warnings tests/test_controllers.py  -k 'test_add_user' --capture=sys`



## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
- [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [FLask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
