# -*- coding:utf-8 -*-  

"""
- Author: Xiao Liu
- Create a list of these movie objects
"""

import media
import fresh_tomatoes

# - Create instance for Movie: title, storyline, poster_image_url, trailer_youtube_url

THE_HERO = media.Movie(
	"The Hero", 
	"Sam Elliott plays an ailing movie star coming to terms with his past and mortality in the first trailer for Brett Haley’s Sundance dramedy The Hero, out in U.S. theaters on June 9th.", 
	"https://i.ytimg.com/vi/SNV99cRiNDY/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=68&sigh=AZ2ND11ImQd8VTWghse401vOzyI",
	"https://www.youtube.com/watch?v=SNV99cRiNDY")


THE_DARK_TOWER = media.Movie(
	"The Dark Tower", 
	"There are other worlds than these. Stephen King’s The Dark Tower, the ambitious and expansive story from one of the world’s most celebrated authors, makes its launch to the big screen. The last Gunslinger, Roland Deschain (Idris Elba), has been locked in an eternal battle with Walter O’Dim, also known as the Man in Black (Matthew McConaughey), determined to prevent him from toppling the Dark Tower, which holds the universe together. With the fate of the worlds at stake, good and evil will collide in the ultimate battle as only Roland can defend the Tower from the Man in Black.", 
	"https://i.ytimg.com/vi/GjwfqXTebIY/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=67&sigh=6OlFj_tIqefyCXebRXLuED8mdmI",
	"https://www.youtube.com/watch?v=GjwfqXTebIY")

CHURCHILL = media.Movie(
	"Churchill", 
	"FilmTrailerZone is the #1 destination for all movie fans to catch the latest movie trailers, clips, featurettes & much more of the latest promotional content from your most anticipated movies!", 
	"https://i.ytimg.com/vi/sVOzMZ4IrMA/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=67&sigh=rDXtr7TsSHxjFQvVoh90HmpWleA",
	"https://www.youtube.com/watch?v=sVOzMZ4IrMA")


movies = [THE_HERO, THE_DARK_TOWER, CHURCHILL]
fresh_tomatoes.open_movies_page(movies)



