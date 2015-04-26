class Movie(object):
    """Class that represents a movie"""

    def __init__(self, title, poster_image_url, trailer_youtube_url, director, actors, release_date):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.actors = actors
        self.release_date = release_date
