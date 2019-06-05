class Movie:
    # title
    # rating
    # year
    def __init__(self, title, rating, year, director="Stanley Kubrik"):
        # string
        self.title = title
        # string
        self.rating = rating
        # int
        self.year = year
        # string
        self.director = director

    def display_attributes(self):
        print(f"Title: {self.title}, Rating: {self.rating}, Released: {self.year}, Director: {self.director}")

class MovieTheater:
    def __init__(self, flick):
        # Movie
        self.current_movie = flick
    
    def change_movie(self, movie):
        self.current_movie = movie

    

    

terminator = Movie("Terminator", "R", 1984, "James Cameron")

bambi = Movie("Bambi", "G", 1962)

cineplex = MovieTheater(bambi)

bambi.display_attributes()
