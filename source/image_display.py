# Takes a file name in the directory as an input and displays that image

from PIL import Image

file = input("Type the image file's name: ")
image = Image.open(file)
image.show()
