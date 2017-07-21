import webbrowser

class Movie() :
	""" This class stores movie related information """

	valid_ratings= ['G', 'PG', 'PG-13', 'R']
	def __init__(self, title, storyline, poster_image, youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_url

        def show_trailer(self) :
		webbrowser.open(self.trailer_youtube_url)


