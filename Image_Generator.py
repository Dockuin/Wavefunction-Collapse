from os import listdir
import time
from PIL import Image

size = 196, 42
im = Image.new("RGB",size)

FOLDER = "Circuit/"


## TIMING DECORATOR - @tictoc
def tictoc(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time() - t1
        print(f"{func.__name__} ran in {t2} seconds")
    return wrapper


def tileSetGenerator(directory=FOLDER):
    imageSet = listdir(directory)
    imageSetDICT = {}
    for tile in imageSet:
        imageSetDICT[tile.removesuffix(".png")] = tile
    return imageSetDICT, imageSet

tileSet, imageSet = tileSetGenerator()

coordinate_x, coordinate_y = 0, 0


for xlimit in range(14):
    activeImage = Image.open(f"{FOLDER}/{imageSet[xlimit]}")
    activeImage.copy()

    for ylimit in range(3): 
        im.paste(activeImage, (coordinate_x, coordinate_y))
        coordinate_y += 14

    coordinate_y = 0
    coordinate_x += 14

im.show()
# im.save("dskewgridFULL.png")







