#! python 2.7.9

import fresh_tomatoes
import media



toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=_KFpws6qmuw")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

top_gun = media.Movie(
    "Top Gun",
    "F14 piolots jam it up",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)

ratatouille = media.Movie(
    "Ratatouille",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Romantic drama",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)

hunger_games = media.Movie(
    "Hunger Games - Mockingjay",
    "F14 pilots jam it up",
    "http://upload.wikimedia.org/wikipedia/en/c/cc/Mockingjay.JPG",
    "https://www.youtube.com/watch?v=vwBbrngafl0"
)

movies = [toy_story, top_gun, avatar, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)