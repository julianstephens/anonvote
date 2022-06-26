import shortuuid

from .extensions import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_modified = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, name):
        self.name = name


class Poll(BaseModel):
    __tablename__ = "polls"

    url_slug = db.Column(
        db.String,
        default=str(shortuuid.uuid()),
        unique=True,
        nullable=False,
    )
    description = db.Column(db.String)
    items = db.relationship("Item", backref="polls", lazy=True)

    def __init__(self, name, description=None):
        super(Poll, self).__init__(name)
        self.description = description

    def __repr__(self):
        return "<Poll %r>" % self.name

    def _to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "slug": self.url_slug,
            "items": self.items,
        }


class Item(BaseModel):
    __tablename__ = "items"

    poll_id = db.Column(db.Integer, db.ForeignKey("polls.id"), nullable=False)

    def __init__(self, name):
        super(Item, self).__init__(name)

    def __repr__(self):
        return "<Item %r>" % self.name

    def _to_json(self):
        return {"name": self.name, "description": self.description}
