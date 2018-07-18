import media # this is the file which contain Movie class
import fresh_tomatoes # we download this file and put it in the same path
Toy_story = media.Movie("Toy Story","Toy story story line","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
last_Last_Samurai = media.Movie("The Last Samurai ","Captain Nathan Algren, a bitter alcoholic traumatized by the atrocities he committed during the American Indian Wars, is approached by his former commanding officer Colonel Bagley to train the newly created Imperial Japanese Army","https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg","https://www.youtube.com/watch?v=T50_qHEOahQ")
Avatar = media.Movie("Avatar (2009 film)","In 2154, humans have depleted Earth's natural resources, leading to a severe energy crisis.","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=6ziBFh3V1aM&t=8s")
Martian = media.Movie("The Martian (film)","The film, produced through 20th Century Fox, is a co-production of the United States and the United Kingdom.[2] Producer Simon Kinberg began developing the film after Fox ","https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg","https://www.youtube.com/watch?v=ej3ioOneTy8")
#print toy_story.storyline
#last_Last_Samurai.show_trailer()
movies = [Toy_story,last_Last_Samurai,Avatar,Martian,Toy_story,Avatar]
#fresh_tomatoes.open_movies_page(movies)
print Avatar.__class__
print Avatar.__dict__
#print media.Movie.__dict__
print media.Movie.__doc__

