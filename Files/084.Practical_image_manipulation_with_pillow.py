# -------------------------------------------------
# -- Practical => image maniputation with pillow --
# -------------------------------------------------

from PIL import Image

# Open the image 
my_image = Image.open(r"D:\Test\pythonlogo.png")

# Show the image 
my_image.Show()

# My cropped image 
my_box = (0, 0, 400, 400)
my_box = (300, 300, 800, 800)
# my_box = (left, upper, top, lower)
my_new_image = my_image.crop(my_box)

# Show the new image 
my_new_image.show()


# Converted mode image 
my_converted = my_image.convert("L")
my_converted.show()
