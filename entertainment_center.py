import media
import fresh_tomatoes


toy_story  = media.Movie("Toy Story",
		          "A story of a boy and his toys that come to life",
			  "https://lumiere-a.akamaihd.net/v1/images/c3c2b4a3323c4a71929cd5fc76bcda4df7157175.jpeg?region=0%2C0%2C1024%2C320",
			  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
		     "The story of Pandora and its inhabitants and their fight to keep their way of life",
		     "http://www.avatarmovie.com/assets/images/photo-1.jpg",
		     "https://youtu.be/1EnL7vUmvQ4")

satya = media.Movie("Satya",
		     "The story of Satys who comes to Mumbai in search of work and gets embroiled in thein its underbelly - the Mumbai underworld",
		     
		     "https://upload.wikimedia.org/wikipedia/en/1/12/Satya.jpg",
		     "https://www.youtube.com/watch?v=CJlrrBZAatM")

gwh = media.Movie("Good Will Hunting",
		     "The story of Will Hunting a genius kid from  the Boston South and his journey to finding himself with the help of Sean, a therapist",
		     
		     "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
		     "https://www.youtube.com/watch?v=QSMvyuEeIyw")
# list collection of movies
MOVIES = [toy_story, avatar, satya, gwh]

# launch the web page to show movies
fresh_tomatoes.open_movies_page(MOVIES)

