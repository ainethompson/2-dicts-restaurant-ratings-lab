"""Restaurant rating lister."""


def get_ratings(filename):

    ratings = {}

    for line in open(filename):
        data = line.rstrip().split(':')

        ratings[data[0]] = data[1]


    for item in sorted(ratings.items()):
        print(f"{item[0]} is rated at {item[1]}")

get_ratings('scores.txt')