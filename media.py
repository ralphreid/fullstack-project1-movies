import webbrowser

__author__ = 'ralph'


class Movie():
    """ This class provides a way to store movie related
    information
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_story_line, movie_poster_image_url, movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)