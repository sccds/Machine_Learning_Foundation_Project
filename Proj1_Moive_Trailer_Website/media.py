# -*- coding:utf-8 -*-

"""
- Author: Xiao Liu
- Write a movie class: properties of a movie 
- Include movie titles, box art, poster images, and movie trailer URLs, 
	and number of views(additional)
"""

import webbrowser
import urllib2
from bs4 import BeautifulSoup


class Movie():

    """
        Initialize Movie instance
        Input: title, storyline, poster_image_url, trailer_youtube_url, num_views
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.num_views = ""

    def show_trailer(self):
    	"""
			open a web window, connect to trailer youtube url
    	"""
        webbrowser.open(self.trailer_youtube_url)

    def get_number_views(self):
    	"""
			Crawl movie trailer youtube page
			Parse view count using BeautifulSoup
    	"""
        response = urllib2.urlopen(self.trailer_youtube_url)
        soup = BeautifulSoup(response.read(), "html.parser")
        view_count = soup.find('div', class_="watch-view-count").get_text()
        return view_count.encode('utf-8').strip()
