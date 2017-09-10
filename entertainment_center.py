import media
import fresh_tomatoes

toy_story =  media.Movie("Toy Story",
			"A story of a boy and his toys that come to life",
			"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
		"A marine on a alien planet",
		"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
		"https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
			"Storyline",
			"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
			"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
			"Storyline",
			"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
			"https://www.youtube.com/watch?v=uVeNEbh3A4U")

midnight_in_paris = media.Movie("Midnight in Paris",
				"Storyline",
				"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
				"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
			"Storyline",
			"https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
			"https://www.youtube.com/watch?v=MkvUNfySGQU")


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games ]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
