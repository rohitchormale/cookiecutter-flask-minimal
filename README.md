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


## Bootstrapping

By default, development environment is not enabled. To enable it, set environmental variable 'FLASK_ENV=development'.


## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
- [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [FLask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
