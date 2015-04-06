import fresh_tomatoes

__author__ = 'ralph'

import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=_KFpws6qmuw")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

top_gun = media.Movie(
    "Top Gun",
    "F14 piolots jam it up",
    "http://en.wikipedia.org/wiki/File:Top_Gun_Movie.jpg",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)

ratatouille = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

midnight_in_paris = media.Movie(
    "Top Gun",
    "F14 piolots jam it up",
    "http://en.wikipedia.org/wiki/File:Top_Gun_Movie.jpg",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)

hunger_games = media.Movie(
    "Top Gun",
    "F14 piolots jam it up",
    "http://en.wikipedia.org/wiki/File:Top_Gun_Movie.jpg",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)




movies = [toy_story, top_gun, avatar, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)