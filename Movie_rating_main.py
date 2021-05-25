from Movie_rating import Movie_rating
from Movierating_Check import User_Check

class Movie_rating_main(Movie_rating, User_Check):

    def __init__(self):
        super().__init__()

    def Movie_Rating_main(self):
        while True:
            print("You can choose from the following")
            for ratings in Movie_rating.Movie_List.keys():
                print(ratings)
            user_rating = input("What rating do you want to know about?  ").lower()
            if Movie_rating_main.User_Exit(user_rating):
                return True
            elif not Movie_rating_main.User_Exit(user_rating):
                return False


    def User_Exit(User):
        if User() == "exit":
            return False
        else:
            print("Please enter a valid movie rating")

    def User_Input(User):

        if User in Movie_rating.Movie_List.keys():
            if User_Check(User):
                if input("Do you want to see another one? Y/N  ").upper() == "Y":
                    print("\n")
                    return True
                else:
                    return False

Movie_rating_main().Movie_Rating_main()