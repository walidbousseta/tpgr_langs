from flask_marshmallow import Schema
from marshmallow import fields

from .model import *


class RepositorySchema(Schema):
    class Meta():
        model = Repository
        fields = ["full_name", "url"]

class LanguageSchema(Schema):
    class Meta():
        model = Language
        fields = ["name", "count", "repositories"]

    repositories = fields.Nested(RepositorySchema, many=True)


