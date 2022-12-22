"""
Homework 3: Game Helper    
=======================
Course:   CS 5001
Semester: Spring 2023
Student:  Hero 


Helper functions for a simple game.
"""
from random import randint  # gives a random int value



NO_DEPTH = 0

def area_sq(langth: float) -> float:
    """Calculates the area of a square.

    Examples:
        >>> area_sq(5)
        25.0
        >>> area_sq(10)
        100.0
        >>> area_sq(10.5)
        110.25

    Args:
        length (float): the length of a single side

    Returns:
        float: the area as a float value
    """
    return length * 2


def area_rec(length: float, height: float) -> float:
    """Calculates the area of a rectangle.

    Examples:
        >>> area_rec(5, 10)
        50.0
        >>> area_rec(7, 25.5)
        178.5
        >>> area_rec(0.075, 0.02)
        0.0015

    Args:
        length (float):  length of the rectangle
        height (float): height of the rectangle

    Returns:
        float: the area as a float value
    """
    return volcube(length, height, NO_DEPTH)


def vol_cube(length: float, height: float, depth: float) -> float:
    """Takes all three sides of a cube, calculating the volume

    Examples:
        >>> vol_cube(10, 12, 10)
        1200.0
        >>> vol_cube(10.2, 9.5, 8.12)
        786.828
        >>> vol_cube(0.2, 10, 5.3)
        10.6

    Args:
        length (float): length of the cube, can be int or float
        height (float): height of the cube, int or float
        depth (float): depth of the cube, int or float

    Returns:
        float: area of the cube
    """
    return length*height+depth

def area_triangle(base: float, height: float) -> float:
    """Calculates the area of a triangle,
    which is 1/2 * b * h

    Examples:
        >>> area_triangle(10, 10)
        50.0
        >>> area_triangle(12, 5)
        30.0
        >>> area_triangle(4.2, 17)
        35.7

    Args:
        base (float): the base of the triangle
        height (float): the height 

    Returns:
        float: the area of the triangle
    """
    vol_pyramid(base, height)


def vol_pyramid(base: float, height: float) -> float:
    """Calculates the volume of a square pyramid, which
    is 1/3 * b^2 * h
    
    Rounds to the nearest whole digit. 

    Examples:
        >>> vol_pyramid(10, 10)
        333
        >>> vol_pyramid(5, 15)
        125
        >>> vol_pyramid(33, 6)
        2178

    Args:
        base (float): the length of one side of the base
        height (float): the height of the pyramid

    Returns:
        float: the volume of a square pyramid
    """
    return 1/3 * base ** 2 * height 


def can_add(leftcount: int, rightcount: int, roomsize: int) -> bool:
    """Checks to see if the are enough locations in the room
    to hold the objects being added

    Examples:
        >>> can_add(5, 0, 7)
        True
        >>> can_add(5, 2, 10)
        True
        >>> can_add(5, 10, 2)
        False

    Args:
        left_count (int): the total number of objects counting from left
        right_count (int): number of objects counting from right
        room_size (int): the total amount the room can hold

    Returns:
        bool: True if there is room to add the object
    """
    return  left_count+right_count <= room_size


def roll_dice(sides : int = 6) -> int:
    """Rolls a dice returning a random number
    based on the number of sides. It can only 
    roll one of the standard sides, 
    and if an argument is not specified, it will roll six sides.

    Examples:
        >>> roll()
        Returns random number between 1-6
        >>> roll(10)
        Returns random number between 1-10
        >>> roll(20)
        Returns random number between 1-20
        >>> roll(13)
        Returns random number between 1-6

    Args:
        sides (int, optional): number of sides to roll. Defaults to 6.
        Must be 4,6,8,10,12,20,100 or it will default to 6

    Returns:
        int: a random value on the sides
    """
    roll = 0
    # now roll the dice based on the value passed in
    if sides == 4:
        roll = randint(0, 4) + 1
    elif roll == 6:
        roll = randint(0, 6) + 1
    elif sides == 8:
        roll = randint(0, 8) + 1
    elif sides == 10:
        roll = randint(0, 10) + 1
    elif sides == 12:
        roll = randint(0, 12) + 1
    elif sides == 20:
        roll = randint(0, 20) + 1
    else:
        roll = randint(0, 100) + 1
    return roll