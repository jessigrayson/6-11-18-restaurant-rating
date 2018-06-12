"""Restaurant rating lister."""


def change_to_dictionary(filename):

    restaurant_rating_dict = {}

    for line in open(filename):
        line = line.strip()
        line = line.split(':')
        restaurant = line[0]
        rating = line[1]
        restaurant_rating_dict[restaurant] = rating

    return restaurant_rating_dict


def print_sorted_dict(restaurant_rating_dict):

    restaurants_lst = sorted(restaurant_rating_dict)

    for eatery in restaurants_lst:
        print("{} is rated at {}.".format(
            eatery, restaurant_rating_dict[eatery])
        )


def run_program(filename):

    restaurant_rating_dict = change_to_dictionary(filename)

    want_to_add = True

    while want_to_add:
        answer = input("Do you want to add a resturant score? (Y/N): ")

        if answer == "Y":
            new_resturant = input("What restaurant do you want to add? ")
            new_resturant_score = input("Enter a rating for your restaurant: ")
            restaurant_rating_dict[new_resturant] = new_resturant_score

        else:
            want_to_add = False

    print_sorted_dict(restaurant_rating_dict)


run_program("scores.txt")
