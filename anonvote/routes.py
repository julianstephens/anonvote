from flask import Blueprint, redirect, render_template, request, flash, url_for

from .extensions import db
from .models import Item, Poll
from .forms import ItemForm, PollForm
import logging

poll_bp = Blueprint("poll", __name__, url_prefix="/polls")

logger = logging.getLogger("werkzeug")


@poll_bp.route("/", methods=["GET", "POST"])
def create_poll():
    form = PollForm()
    poll = None

    if request.method == "GET":
        return render_template("index.jinja", form=form)

    if form.validate_on_submit():
        poll = Poll(form.name.data, form.description.data)
    else:
        flash("Hmm something doesn't look right here. Please double check your form fields.", "error")
        return redirect(url_for("index"))

    try:
        db.session.add(poll)
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash("Oops something went wrong creating your poll. Please try again", "error")
        return redirect(url_for("index"))
    
    return redirect(url_for("poll.polls", poll_id=poll.id))

@poll_bp.route("/<poll_id>")
@poll_bp.route("/<poll_id>/<item_id>", methods=["POST", "PUT", "DELETE"])
def polls(poll_id, item_id=None):
    try:
        poll_id = int(poll_id)
    except ValueError:
        pass

    form = ItemForm()
    poll = _get_poll(poll_id)

    if not poll:
        flash("Hmmm we couldn't find that poll. Try using a different ID.", "error")
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("poll.jinja", poll=poll._to_json(), items=poll.items, form=form)

    # if request.method == "POST":

    if request.method == "PUT":
        updated_poll = poll
        updated_poll.name = request.form.get("name") or poll.name
        updated_poll.description = request.form.get("description") or poll.description

        try:
            db.session.add(updated_poll)
            db.session.commit()
            return render_template(
                "poll.jinja", poll=updated_poll._to_json(), items=updated_poll.items
            )
        except Exception:
            flash("Something went wrong updating your poll. Please try again", "error")
            return render_template("poll.jinja", poll=poll._to_json(), items=poll.items)


def _get_poll(id, only_id=False):
    """Retrieves poll by pk or url slug

    Args:
        id (int|string): id to query by

    Returns:
        Poll
    """
    poll = None
    try:
        if isinstance(id, int):
            poll = Poll.query.filter_by(id=id).first_or_404()
        else:
            poll = Poll.query.filter_by(url_slug=id).first_or_404()

        return poll.id if only_id else poll
    except:
        return None
