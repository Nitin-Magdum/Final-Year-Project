

from PIL import Image

#read the image
im = Image.open("sample-image.png")

#rotate image by 90 degrees
angle = 90
out = im.rotate(angle, expand=True)
out.save('rotate-output.png')
