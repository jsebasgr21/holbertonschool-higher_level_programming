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


@property
def height(self):
    return self.__height


@height.setter
def height(self, value):
    if type(height) is not int:
        raise TypeError("height must be an integer")
    elif height < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = height
