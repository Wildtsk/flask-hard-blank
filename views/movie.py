import flask
from flask import request
from flask_restx import Resource, Namespace

from dao.model.schemas import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        args = flask.request.args
        if len(args):
            return movie_schema.dump(
                movie_service.get_movie_by_kwargs(**args)
            ), 200

        return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        if movie_service.create_movie(**flask.request.json):
            return "Фильм создан", 200
        else:
            return "Фильм не создан, ошибка", 200


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        return movie_schema.dump(movie_service.get_movie_by_id(uid=uid)), 200

    def put(self, uid):
        if movie_service.get_update_movie(**flask.request.json):
            return "Фильм обновлен", 200
        else:
            return "Фильм не обновлен, ошибка", 200

    def delete(self, uid):
        if movie_service.get_delete_movie(uid):
            return "Фильм удален", 200
        else:
            return "Фильм не удален, ошибка", 200