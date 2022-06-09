from marshmallow import Schema, fields


class PollSchema(Schema):
    id = fields.Int(dump_only=True)
    uuid = fields.UUID(allow_none=False)
    name = fields.Str(allow_none=False)
    date_created = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)


class PollItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(allow_none=False)
    poll = fields.Nested(PollSchema, allow_none=True)
    date_created = fields.DateTime(dump_only=True)
    date_modified = fields.DateTime(dump_only=True)
