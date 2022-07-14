"""
File: stanCodoshop.py
Name: Leticia Chen
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # A math formula to calculate distance between 2 pixels
    dist = (red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2
    color_distance = math.sqrt(dist)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Pixels = [p1, p2, p3,...]
    t_r = 0                                 # sum of red color
    t_g = 0                                 # sum of green color
    t_b = 0                                 # sum of blue color
    for i in range(len(pixels)):            # Run every pixel of list
        t_r += pixels[i].red
        t_g += pixels[i].green
        t_b += pixels[i].blue
    avg_r = t_r//(len(pixels))              # Get average of every color
    avg_g = t_g//(len(pixels))
    avg_b = t_b//(len(pixels))

    return [avg_r, avg_g, avg_b]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # Pixels = [p1, p2, p3,...]
    avg_pixel = get_average(pixels)                         # [avg_r, avg_g, avg_b]
    red = avg_pixel[0]
    green = avg_pixel[1]
    blue = avg_pixel[2]

    # First Data(pixel) to start comparing with average RGB(red, green, blue)
    best_dist = get_pixel_dist(pixels[0], red, green, blue)
    best_pixel = pixels[0]

    # To start comparing distances between the rest pixels and get the best pixel if they are smallest distance
    for i in range(1, len(pixels)):
        pixels_dist = get_pixel_dist(pixels[i], red, green, blue)
        if pixels_dist < best_dist:
            best_dist = pixels_dist
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # images = [SimpleImage('156-500.jpg'),...]
    for x in range(width):
        for y in range(height):
            pixels = []                                 # List to get pixels at the same position form images
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)                    # If there are 3 images, will have 3 pixels at the same position

            final_pixel = get_best_pixel(pixels)        # After get pixels(from 3 images) in one point(x,y), find the best

            # To start forming new picture without person, animal...
            new_pixel = result.get_pixel(x, y)
            new_pixel.red = final_pixel.red
            new_pixel.green = final_pixel.green
            new_pixel.blue = final_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):                       # dir: directory
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)            # images = [SimpleImage('156-500.jpg'),...]
    return images


def main():

    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
