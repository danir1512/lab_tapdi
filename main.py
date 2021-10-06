import cv2 as cv
import tkinter as tk
import tkinter.filedialog as window
import imageForms as forms
#root = tk.Tk()
#root.withdraw()
#file_path = window.askopenfilename()

# abrir imagem
pathname = "/Users/d.genovse/Desktop/TAPDI/"
filename = "peppers.jpeg"
img = cv.imread(pathname + filename)

#if file_path != "":
#img = cv.imread(file_path)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, imgBW = cv.threshold(imgGray, 12, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
#forms.showSideBySideImages(imgGray,imgBW,"teste")
imgBlur = cv.blur(img,(11,11))
dimensions = img.shape

'''
isto é um teste
'''


cv.imshow("Imagem", imgBlur)
#cv.imshow("Imagem", imgBW)
cv.waitKey()



