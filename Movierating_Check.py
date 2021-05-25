from Movie_rating import Movie_rating
from Movie_rating_main import Movie_rating_main


print(Movie_rating.Movie_List)

class User_Check(Movie_rating, Movie_rating_main):
    def __init__(self):
        super().__init__()

    def User_Check(Age):

        if Age == "exit":
            return False
        elif Age == "u":
            print(Movie_rating().Movie_List["u"])
            return True
        elif Age == "pg":
            print(Movie_rating().Movie_List["pg"])
            return True
        elif Age == "12":
            print(Movie_rating().Movie_List["12"])
            return True
        elif Age == "15":
            print(Movie_rating().Movie_List["15"])
            return True
        elif Age == "18":
            print(Movie_rating().Movie_List["18"])
            return True

