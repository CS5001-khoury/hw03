""" 
Student: YOUR_NAME
Term: SEMESTER

Compares two colors, both normal, and with various color blindness conditions applied

"""
import math

MIN_DIFFERENCE = .20


# provided functions, no need to change

def delta(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> float:
    """Uses the following formula to compare two different colors. This
    is a simplified way to compare two colors as it doesn't take
    into account hue or saturation differences. If you are curious
    about a more standard approach, one should look up the CIEDE2000 formula. 

    euclidean = (R_1 - R_2)^2 + (G_1 - G_2)^2 + (B_1 - B2)^2
    euclidean = sqrt(euclidean)  # the two lines are known as the euclidean distance and common for a lot of things
    scaled = floor(euclidean) / 441  #scales the distance between 0 and 1

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color


    Returns:
        float: a value between 0 and 1, representing how different colors are. Lower numbers are more similar. 
    """
    return int(math.sqrt((red_one - red_two) ** 2 + 
                         (green_one - green_two) ** 2 + 
                         (blue_one - blue_two) ** 2)) / 441

def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts an RBG color to a HEX string value often used for HTML color pallets. 

    The conversion format string is  f"#{red:02x}{green:02x}{blue:02x}"

    Args:
        red (int): red color value
        green (int): green color value
        blue (int): blue color value

    Returns:
        str: the formatted string
    """
    return f"#{red:02x}{green:02x}{blue:02x}"

## end provided functions

# add your functions here - remember to indent properly! so def 
# starts on the far side, then everything is indented under for each function, use the other functions as examples


def main():
    """
    Main driver of the program.

    1. Welcomes the client
    2. Prompts them to enter two colors, by asking for the
       RBG values for the first color, and then second. 
    3. Displays the HTML values for the each color including the variations
       they would look like with various types of color blindness.
    4. Runs checks on each of the colors to determine similarity
    5. If the colors are two similar prints "The colors are too similar", 
       or states they are different if they are different enough.
    6. ends program
    """
    # UNCOMMENT lines after you finish the related functions!! 
    # You will probably finish other functions and **test** them
    # well before you uncomment parts of the main!

    # print("Welcome to color checker.")
    # print("Enter the RGB values for two colors.")
    # print("Enter your first color:")
    # red_one = get_number_from_client("Red: ")
    # green_one = get_number_from_client("Green: ")
    # blue_one = get_number_from_client("Blue: ")
    # print("Enter your second color:")
    # red_two = get_number_from_client("Red: ")
    # green_two = get_number_from_client("Green: ")
    # blue_two = get_number_from_client("Blue: ")

    # print("The HTML values for the Color 1 are: ")
    # print_html_values(red_one, green_one, blue_one)
    # print("The HTML values for the Color 2 are: ")
    # print_html_values(red_two, green_two, blue_two)

    # valid = run_checks(red_one, green_one, blue_one, red_two, green_two, blue_two)

    # if valid:
    #    print("The colors are different.")
    # else:
    #    print("The colors are too similar.")



if __name__ == "__main__":
    main()
