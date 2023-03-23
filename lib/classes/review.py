from classes.viewer import Viewer
from classes.movie import Movie

class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        self.add_review_to_viewer()
        self.add_review_to_movie()
        self.add_movie_to_viewer()
        self.add_viewer_to_movie()
        pass

    # rating property goes here!
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 0 < rating < 6:
            self._rating = rating
        else:
            raise Exception ("Rating should be an interger between 1 and 5 inclusive!")

    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception ("Viewer must be a valid Viewer class object")

    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie must be a valid Movie class object")

    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)

    def add_review_to_movie(self):
        self._movie.reviews.append(self)

    def add_movie_to_viewer(self):
        self._viewer.reviewed_movies.append(self._movie)
    
    def add_viewer_to_movie(self):
        self._movie.reviewers.append(self._viewer)
