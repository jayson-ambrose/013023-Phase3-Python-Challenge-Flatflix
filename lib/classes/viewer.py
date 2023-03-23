class Viewer:

    all_users = []
    
    def __init__(self, username):

        self.username = username
        self.reviews = []
        self.reviewed_movies = []

        Viewer.all_users.append(self.username)

    # username property goes here!
    @property
    def username(self):
        return self._username   

    @username.setter
    def username(self, username):



        if type(username) == str and 5 < len(username) < 17:
            self._username = username
            # Viewer.all_usernames.append(self._username)
        else:
            raise Exception("Username must be a string between 6 and 16 characters inclusive and must be unique!")

    @property
    def reviewed_movies(self):
        return self._reviewed_movies

    @reviewed_movies.setter
    def reviewed_movies(self, reviewed_movies):
        self._reviewed_movies = reviewed_movies

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    def reviewed_movie(self, movie):
        return movie in self.reviewed_movies

    def rate_movie(self, movie, rating):

        from classes.review import Review

        if movie not in self.reviewed_movies:
            Review(self, movie, rating)
        
        else:
            for review in self._reviews:
                if review.movie.title == movie.title:
                    review = Review(self, movie, rating)
            