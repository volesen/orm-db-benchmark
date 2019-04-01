from marshmallow import Schema, fields


class TrackSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    unit_price = fields.Float()


class AlbumSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    price = fields.Int()

    tracks = fields.Nested(TrackSchema(), many=True)


class AuthorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

    publisher = fields.Str()
    address = fields.Str()

    albums = fields.Nested(AlbumSchema(), many=True)
