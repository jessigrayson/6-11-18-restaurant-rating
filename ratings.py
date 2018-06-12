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


def user_add_ratings(restaurant_rating_dict):
    want_to_add = True

    while want_to_add:
        new_resturant = input("What restaurant do you want to add? ")
        new_resturant_score = input("Enter the rating for your restaurant: ")



    restaurant_rating_dict[new_resturant] = restaurant_rating_dict.get(new_resturant, new_resturant_score)

    print_sorted_dict(restaurant_rating_dict)

def run_program(filename)
    
    print_sorted_dict(change_to_dictionary("scores.txt"))
    user_add_ratings(restaurant_rating_dict)
    
    answer = input("Do you want to add another/new_resturant_score? (Y/N): ")
    
    if answer is "Y":
        want_to_add = True
    else:
        False

run_program("scores.txt")