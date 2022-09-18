# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.models import Director


# Например

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        return self.session.query(Director).all()

    def det_director(self, uid):
        return self.session.query(Director).get(uid)