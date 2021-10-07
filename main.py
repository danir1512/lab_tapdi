import cv2 as cv
import tkinter as tk
import tkinter.filedialog as fd
import imageForms as IF

#abrir imagem
root = tk.Tk()
root.withdraw()
file_path = fd.askopenfilename()

img = cv.imread(file_path)
newImg = img
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,imgBW = cv.threshold(imgGray, 12, 255, cv.THRESH_BINARY, cv.THRESH_OTSU)
IF.showSideBySideImages(img, imgGray, "Imagens", False, False)
imgBlur = cv.blur(img, (3,3))

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

brightness = input("Brightness: ")
contrast = input("Contrast: ")

for x in range(height):
    for y in range(width):
        for z in range(3):
            newBit = int(img[x, y, z] * contrast + brightness)
            if newBit > 255:
                newBit = 255
            elif newBit < 0:
                newBit = 0
            else:
                newImg[x,y,z] = newBit

cv.imshow("Imagem", newImg)
cv.waitKey()