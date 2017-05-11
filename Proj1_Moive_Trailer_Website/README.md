# Project: Movie Trailer Website
## Udacity Machine Learning Foundation Nanodegree Program

----
#### Xiao Liu
----

- The file `fresh_tomatoes.py` contains the `open_movies_page()`` function that will take in your list of movies and generate an HTML file including this content, producing a website to showcase your favorite movies.

- Your task is to write a movie class in `media.py`. To do this, think about what the properties of a movie are that need to be encapsulated in a movie object such as movie titles, box art, poster images, and movie trailer URLs. Look at what `open_movies_page()` does with a list of movie objects for hints on how to design your movie class.

- You’ll want to write a constructor for the movie class so that you can create instances of movie. You can now create a list of these movie objects in `entertainment_center.py` by calling the constructor `media.Movie()` to instantiate movie objects. You’ve given movies their own custom data structure by defining the movie class and constructor, and now these objects can be stored in a list data structure. This list of movies is what the `open_movies_page()` function needs as input in order to build the HTML file, so you can display your website.