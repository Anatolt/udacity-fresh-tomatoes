import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
	"The story of a boy and his toys that come to lofe",
	"https://upload.wikimedia.org/wikipedia/ru/a/a6/Toy_Story_1995_Poster.jpg",
	"http://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/ru/thumb/4/4b/Avatar-2009.jpg/640px-Avatar-2009.jpg",
	"http://www.youtube.com/watch?v=cRdxXPV9GNQ")

equilibrium = media.Movie("Equilibrium",
	"In a Fascist future where all forms of feeling are illegal",
	"https://upload.wikimedia.org/wikipedia/ru/4/4f/Equilibrium.jpg",
	"http://www.youtube.com/watch?v=ZVDiaYQXBVs")

big_lebowski = media.Movie("The Big Lebowski",
                           "Times Like These Call For A Big Lebowski",
                           "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")

got = media.Movie("Game of Thrones",
                     "7 powerful Houses are fighting for the Iron Throne of 7 Kingdoms",
                     "http://4.bp.blogspot.com/-FuP3ehGClQs/TfBm4yiOSVI/AAAAAAAAA38/6Wgx0eijnKI/s1600/600full-game-of-thrones-poster.jpg",
                     "http://www.youtube.com/watch?v=BpJYNVhGf1s")

monster = media.Movie("Monsters University", 
                 "A look at the relationship between Mike and Sulley at Monsters University",
                 "http://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg",
                 "http://www.youtube.com/watch?v=xBzPioph8CI")

movies = [toy_story, avatar, equilibrium, big_lebowski, got, monster]
fresh_tomatoes.open_movies_page(movies)
