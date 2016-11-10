from tkinter import *
from picamera import PiCamera
from camera import WicCamera

## from PIL import Image, ImageTk

##
##image = Image.open("/home/pi/Desktop/image-2016-10-24-12:08:18.gif")
##photo = ImageTk.PhotoImage(image)
##
##x = Tk()
##
##canvas = Canvas(x)
##canvas.grid(row = 0, column = 0)
##y = PhotoImage(file = photo)
##canvas.create_image(0,0,image= y)
####canvas.pack()
##x.mainloop()

##root = Tk()
##img = PhotoImage(file="/home/pi/Desktop/image-2016-10-24-12:08:18.gif")
##img = img.subsample(2,2)
##w1 = Label(root, image = img).pack(side="right")
##explanation = "At present, only GIF and PPM/PGM formats are supported,"
##w2 = Label(root, justify = LEFT, padx = 10, text = explanation). pack(side = "left")
##root.mainloop()

cam = WicCamera()

##def snapshot():
##    cam.takePicture()

cam.preview()
root = Tk()
##imgFrame = Frame(root)
img = PhotoImage(file = "/home/pi/Desktop/cuteWelcome.gif")
w1 = Label(root, image = img)
w1.grid(row = 0, column = 1)

w2 = Button(root, text = "Take Picture", command = cam.takePicture)
w2.grid(row = 2, column = 0, pady = 15, padx = 10)

w3 = Button(root, text = "Cartoon", command = cam.takeCartoon)
w3.grid(row = 2, column = 1)

w4 = Button(root, text = "Pastel", command = cam.takePastel)
w4.grid(row = 2, column = 2, pady = 15, padx = 10)

w5 = Label(root, text = "Please choose a filter.  You have 5 seconds to pose!")
w5.grid(row = 1, column = 1, pady = 10)

root.mainloop()

##img = img.subsample(2,2)
##w1 = Label(root, image = img).pack(side="top")
##explanation = "At present, only GIF and PPM/PGM formats are supported,"
##w2 = Label(root, justify = LEFT, padx = 10). pack(side = "left")
##w2 = Button(root, text = "Take Picture", command = snapshot).pack(side="bottom")
##w3 = Button(root, text = "New Button", command = snapshot).pack(side="bottom")


