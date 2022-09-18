import flask
from flask_restx import Resource, Namespace

from dao.model.schemas import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        return genre_schema.dump(genre_service.get_genre_by_id(uid=uid)), 200