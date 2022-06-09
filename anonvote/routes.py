from flask import Blueprint, render_template, request, jsonify

from .extensions import db
from .models import Item, Poll


poll_bp = Blueprint("poll", __name__, url_prefix="/polls")
item_bp = Blueprint("item", __name__, url_prefix="/items")

@poll_bp.route("/<int:poll_id>", methods=["GET", "POST", "PUT"])
@poll_bp.route("/", methods=["GET", "POST"])
def poll(poll_id=None):
    data = Poll.fs_get_delete_put_post(poll_id)
    return data

@item_bp.route("/<int:item_id>", methods=["PUT", "DELETE"])
@item_bp.route("/", methods=["POST"])
def item(item_id=None):
    data = Item.fs_get_delete_put_post(item_id)
    return data