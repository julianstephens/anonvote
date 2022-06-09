from flask_serialize import FlaskSerialize
import shortuuid

from .extensions import db

fs_mixin = FlaskSerialize(db)


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_modified = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )


class Poll(fs_mixin, BaseModel):
    __tablename__ = "polls"

    url_string = db.Column(
        db.String,
        default=str(shortuuid.uuid()),
        unique=True,
        nullable=False,
    )
    description = db.Column(db.String)
    items = db.relationship("Item", backref="polls", lazy=True)

    __fs_timestamp_fields__ = ["date_modified"]
    __fs_create_fields__ = __fs_update_fields__ = ["name", "description"]
    __fs_exclude_serialize_fields__ = ["id", "date_created", "date_modified"]
    __fs_update_properties__ = ["name", "description", "url_string"]
    __fs_relationship_fields__ = ["items"]

    def __fs_can_delete(self):
        raise Exception("Deletion not allowed.")

    def __repr__(self):
        return "<Poll %r>" % self.name


class Item(fs_mixin, BaseModel):
    __tablename__ = "items"

    poll_id = db.Column(db.Integer, db.ForeignKey("polls.id"), nullable=False)

    __fs_timestamp_fields__ = ["date_modified"]
    __fs_create_fields__ = ["poll_id", "name"]
    __fs_update_fields__ = ["name"]
    __fs_exclude_serialize_fields__ = ["id", "poll_id", "date_created", "date_modified"]
    __fs_update_properties__ = ["name"]

    def __repr__(self):
        return "<Item %r>" % self.name
