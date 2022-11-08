from PIL import Image

Image.open("wolf.png")

import pywhatkit

pywhatkit.image_to_ascii_art('wolf.png','MyArt')

#reading text file

read_file= open("MyArt.txt","r") 

print(read_file.read())  #clcoding.com
