
"""
- Author: Xiao Liu
- Write a movie class: properties of a movie such as movie titles, box art, poster images, and movie trailer URLs
"""

import webbrowser

class Movie():

	# - Initialize Movie instance
	# - Input: title, storyline, poster_image_url, trailer_youtube_url
	
	def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer():
		webbrowser.open(self.trailer_youtube_url)

