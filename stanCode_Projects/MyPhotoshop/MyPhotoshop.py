"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def main():
    """
    combine 2 photos, space ship photo will be background of figure.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    space_ship.show()
    figure = SimpleImage("images/ReyGreenScreen.png")
    figure.show()
    result = combine(space_ship, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, photo type
    :param figure_img: SimpleImage, photo type
    :return: figure´s background was replaced.
    """
    background = background_img
    figure = figure_img
    for x in range(figure.width):
        for y in range(figure.height):
            figure_pixel = figure.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > bigger * 2:
                background_pixel = background.get_pixel(x, y)
                figure_pixel.red = background_pixel.red
                figure_pixel.green = background_pixel.green
                figure_pixel.blue = background_pixel.blue
    return figure


if __name__ == '__main__':
    main()
