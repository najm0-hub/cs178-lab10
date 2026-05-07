# name: Najmo Mahamed
# date: March Tuesday 3, 2026
# description: Implementation of CRUD operations with DynamoDB — CS178 Lab 10
# proposed score: 0 (out of 5) -- if I don't change this, I agree to get 0 points.

import boto3

# boto3 uses the credentials configured via `aws configure` on EC2
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Movies')

def create_movie():
    title = input("Enter movie title: ").strip()

    table.put_item(
        Item={
            "Title": title,
            "Ratings": []
        }
    )

    print("Movie added successfully.\n")

def print_movie(movie):
    """Print movie details."""
    print("Title:", movie.get("Title"))
    print("Year:", movie.get("Year"))
    print("Genre:", movie.get("Genre", "N/A"))
    print("---------------------")


def print_all_movies():
    """Print all movies in the table."""
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No movies found.")
        return

    print(f"Found {len(items)} movie(s):\n")

def update_rating():
    try:
        title = input("What is the movie title? ")
        rating = int(input("What is the rating (integer): "))

        table.update_item(
            Key={"Title": title},
            UpdateExpression="SET Ratings = list_append(Ratings, :r)",
            ExpressionAttributeValues={":r": [rating]}
        )
    except Exception:
        print("error in updating movie rating")
 

def delete_movie():
    """
    Prompt user for a Movie Title.
    Delete that item from the database.
    """
    print("deleting movie")
    title = input("What is the movie title? ")
    table.delete_item(Key={"Title": title})

def query_movie():
    """
    Prompt user for a Movie Title.
    Print out the average of all ratings in the movie's Ratings list.
    """
    print("query movie")

def print_menu():
    print("----------------------------")
    print("Press C: to CREATE a new movie")
    print("Press R: to READ all movies")
    print("Press U: to UPDATE a movie (add a review)")
    print("Press D: to DELETE a movie")
    print("Press Q: to QUERY a movie's average rating")
    print("Press X: to EXIT application")
    print("----------------------------")

def main():
    input_char = ""
    while input_char.upper() != "X":
        print_menu()
        input_char = input("Choice: ")

        if input_char.upper() == "C":
            create_book()
        elif input_char.upper() == "R":
            read_all_books()
        elif input_char.upper() == "U":
            update_book()
        elif input_char.upper() == "D":
            delete_book()
        elif input_char.upper() == "Q":
            query_book()
        elif input_char.upper() == "X":
            print("exiting...")
        else:
            print("Not a valid option. Try again.")

main()
