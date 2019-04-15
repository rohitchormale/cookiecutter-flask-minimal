from .extensions import db


################
# Helper models
################


class BaseModel(db.Model):
    """
    Abstract model
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, key)
                setattr(self, key, value)
            except AttributeError:
                pass

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


# TODO - Add your models here  e.g.
# class User(BaseModel):
#     pass
