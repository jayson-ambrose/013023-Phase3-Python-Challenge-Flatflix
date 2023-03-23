class Movie:

    all = []
    
    def __init__(self, title):
        
        self.title = title

        self.reviews = []
        self.reviewers = []

        Movie.all.append(self)

    @property
    def title (self):
        return self._title

    @title.setter
    def title (self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception ("Title must be a string with greater than 0 characters")

    def average_rating(self):
        sum = 0
        for review in self.reviews:
            sum = sum + review.rating
        average = sum / len(self.reviews)
        return average

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    @property
    def reviewers(self):
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        self._reviewers = reviewers

    @classmethod
    def highest_rated(cls):

        highest_rated_title = ""
        highest_rating = 0

        for movie in cls.all:
            if movie.average_rating() > highest_rating:
                highest_rated_title = movie.title
                highest_rating = movie.average_rating()

        for movie in cls.all:
            if highest_rated_title == movie.title:
                return movie

