import pandas as pd

class MovieReviewApp:
    def __init__(self):
        self.movie_data = pd.DataFrame(columns=['Movie Name', 'Genre', 'Rating'])

    def add_movie(self, movie_name, genre, rating):
        new_data = pd.DataFrame([[movie_name, genre, rating]], columns=['Movie Name', 'Genre', 'Rating'])
        self.movie_data = pd.concat([self.movie_data, new_data], ignore_index=True)
        print(f"{movie_name} added successfully.")

    def list_reviews(self):
        if len(self.movie_data) == 0:
            print("No reviews yet.")
        else:
            print("\nMovie Reviews:")
            print(self.movie_data)

if __name__ == "__main__":
    app = MovieReviewApp()

    while True:
        print("\nMovie Review Application")
        print("1. Add Movie")
        print("2. List Reviews")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            movie_name = input("Movie Name: ")
            genre = input("Movie Genre: ")
            rating = input("Rating: ")

            app.add_movie(movie_name, genre, rating)
        elif choice == '2':
            app.list_reviews()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid input! Please choose a number between 1 and 3.")
