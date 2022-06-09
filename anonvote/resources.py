from flask import render_template, request
from flask_restful import Resource
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

from anonvote.schemas import PollSchema

from .models import Poll
from .extensions import db


# class PollResource(Resource):
#     def get(self, uuid):
#         poll = Poll.query.filter(uuid=uuid).first_or_404(
#             description=f"There is no poll with id: {uuid}"
#         )
#         return render_template("show_poll.html", poll=poll)

#     def post(self):
#         json_data = request.get_json()
#         if not json_data:
#             return {"message": "No input data provided"}, 400

#         try:
#             data = PollSchema().load(json_data)
#         except ValidationError as err:
#             return err.messages, 422

#         db.session.add(data)
#         db.session.commit()
#         result = PollSchema().dump(Poll.query.get(data.uuid))

#         return {"message": f"Created new poll {poll.uuid}", "poll": result}
