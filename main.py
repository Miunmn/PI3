from PIL import Image

from struct import *

def main():
    number = 0
    for i in range(0,6):
        extension = ".PNG"
        imagename = "Capture"+str(i)
        colorImage  = Image.open("./baseimages/"+imagename+extension)
        transposed  = colorImage.transpose(Image.ROTATE_90)
        transposed1 = colorImage.transpose(Image.ROTATE_180)
        transposed2 = colorImage.transpose(Image.ROTATE_270)
        number = number + 1
        colorImage.save("./allimages/imagen"+str(number)+extension)
        number = number + 1
        transposed1.save("./allimages/imagen"+str(number)+extension)
        number = number + 1
        transposed2.save("./allimages/imagen"+str(number)+extension)
        number = number + 1
        transposed.save("./allimages/imagen"+ str(number)+extension)

if __name__ == "__main__":
    main()