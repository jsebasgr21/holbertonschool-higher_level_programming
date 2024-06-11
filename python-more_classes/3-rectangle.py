#!/usr/bin/python3
"""
This module defines a Rectangle class for representing rectangles.

Classes:
--------
Rectangle
    A class to represent a rectangle with width and height attributes,
    along with appropriate getters and setters that validate the values.
"""


class Rectangle:
    """
    Rectangle class that represents a rectangle.

    Attributes:
    -----------
    width : int
        The width of the rectangle (default is 0).
    height : int
        The height of the rectangle (default is 0).

    Methods:
    --------
    width() -> int
        Getter method for the width attribute.
    width(value: int) -> None
        Setter method for the width attribute.
    height() -> int
        Getter method for the height attribute.
    height(value: int) -> None
        Setter method for the height attribute.
    area() -> int
        Calculates and returns the area of the rectangle.
    perimeter() -> int
        Calculates and returns the perimeter of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle with the given width and height.

        Parameters:
        -----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Parameters:
        -----------
        value : int
            The new value for the width attribute.

        Raises:
        -------
        TypeError:
            If the width is not an integer.
        ValueError:
            If the width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Parameters:
        -----------
        value : int
            The new value for the height attribute.

        Raises:
        -------
        TypeError:
            If the height is not an integer.
        ValueError:
            If the height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        --------
        int:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        If either the width or height is 0, returns 0.

        Returns:
        --------
        int:
        The perimeter of the rectangle,
        or 0 if either the width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle, printing
        it with the character #.
        If either the width or height is 0, returns an empty string.

        Returns:
        --------
        str:
            A string representation of the rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
