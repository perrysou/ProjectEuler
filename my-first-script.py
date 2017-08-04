def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width)  # print top edge of box

    # print sides of box
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")

    print("*" * width)  # print bottom edge of box


def which_prize2(points):
    """
    Returns the number of prize-winning message, given a number of points
    """
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."


def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return top_area + side_area
    else:
        return side_area


def punctuate2(sentence, phrase_type):
    """
    Create a punctuated sentence from a string. Defaults to an ordinary
    sentence with a full stop.

    sentence: string, the phrase that is to have punctuation added
    phrase_type: string, defines what kind of sentence to create.
                "exclamation", "question" and "aside" are known values
    """
    if phrase_type == "exclamation":
        return sentence + "!"
    elif phrase_type == "question":
        return sentence + "?"
    elif phrase_type == "aside":
        return "(" + sentence + ")"
    else:
        return sentence + "."


def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))


def readable_timedelta(days):
    """Print the number of weeks and days in a number of days."""
    # to get the number of weeks we use integer division
    weeks = days // 7
    # to get the number of days that remain we use %, the modulus operator
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


def welcome_message(name, how_many_snakes):
    # Prints out a personalised welcome message
    print("Welcome to this Python script, " + name + "!")
    snake_string = """
    Welcome to Python3!

                 ____
                / . .\\
                \  ---<
                 \  /
       __________/ /
    -=:___________/

    <3, Philip and Charlie
    """

    print(snake_string * how_many_snakes)

# Call the welcome message function with the input "Udacity Student"
# and print the output
welcome_message("Yang", 3)



