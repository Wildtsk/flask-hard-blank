from dao.model.models import Genre


# Например

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        return self.session.query(Genre).all()

    def det_genre(self, uid):
        return self.session.query(Genre).get(uid)