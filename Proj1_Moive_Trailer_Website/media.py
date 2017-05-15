
"""
- Author: Xiao Liu
- Write a movie class: properties of a movie such as movie titles, box art, poster images, and movie trailer URLs, and number of views(additional)
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
        webbrowser.open(self.trailer_youtube_url)

    def get_number_views(self):
        response = urllib2.urlopen(self.trailer_youtube_url)
        soup = BeautifulSoup(response.read(), "html.parser")
        return soup.find('div', class_="watch-view-count").get_text()
