from PIL import Image

from struct import *

def main():
    for i in range(0,6):
        extension = ".PNG"
        imagename = "Capture"+str(i)
        colorImage  = Image.open("./baseimages/"+imagename+extension)
        transposed  = colorImage.transpose(Image.ROTATE_90)
        transposed1 = colorImage.transpose(Image.ROTATE_180)
        transposed2 = colorImage.transpose(Image.ROTATE_270)
        transposed1.save("./allimages/"+imagename+"rot180"+extension)
        transposed2.save("./allimages/"+imagename+"rot270"+extension)
        transposed.save("./allimages/"+imagename+"rot90"+extension)
        colorImage.save("./allimages/"+imagename+extension)

if __name__ == "__main__":
    main()