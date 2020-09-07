# Python script to display all pixels RGB values
# from an image and output them a row at a time
#
# Import the PIL library - pip3 install Pillow
from PIL import Image
 
# Open our image
im = Image.open("original2.png")
 
# Convert our image to RGB
rgb_im = im.convert('RGB')
 
# Use the .size object to retrieve a tuple contain (width,height) of the image
# and assign them to width and height variables
width = rgb_im.size[0]
height = rgb_im.size[1]
 
# set some counters for current row and column and total pixels
row = 1
col = 1
pix = 0
 
# create an empty output row
rowdata = ""
 
# loop through each pixel in each row outputting RGB value as we go...
# all the plus and minus ones are to deal with the .getpixel class being
# zero indexed and we want the output to start at pixel 1,1 not 0,0!
while row < height + 1:
    print("")
    print("Row number: " + str(row))
    while col < width + 1:
        # get the RGB values from the current pixel
        r, g, b = rgb_im.getpixel((col - 1, row - 1))
        # append the RGB values to the rowdata variable as (R, G, B)
        rowdata += "(" + str(r) + "," + str(g) + "," + str(b) + ") "
        # increment the column count
        col = col + 1
        # increment the pixel count
        pix = pix + 1
    # print out all RGB values for the row
    print(rowdata)
    # clear out rowdata variable
    rowdata = ""
    # increment the row...
    row = row + 1
    # reset the column count
    col = 1
 
# output for proof!
print("")
print("Width = " + str(width) + " pixels")
print("Height = " + str(height) + " pixels")
print("Total Pixels = " + str(pix) + ".")
