from dao.model.models import Movie


# Например

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def det_one_movie_by_id(self, uid):
        return self.session.query(Movie).get(uid)

    def get_kwargs(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create_movie(self, **kwargs):
        try:
            self.session.add(Movie(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def update_movie(self, **kwargs):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(kwargs)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False

    def delete_movie(self, uid):
        try:
            movie = self.det_one_movie_by_id(uid)
            self.session.delete(movie)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
