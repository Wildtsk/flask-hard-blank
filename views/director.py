# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

from dao.model.schemas import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        return director_schema.dump(director_service.get_director_by_id(uid=uid)), 200