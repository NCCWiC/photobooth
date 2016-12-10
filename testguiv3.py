from tkinter import *
import os
from time import sleep
from picamera import PiCamera
import picamera
from camera import WicCamera
from gui2 import GUI2
from keyboard import GUIKeyboard

# demo app by Steve O. Working 11/18
# shows gui and cam preview at same time

class MainApplication(Frame):
    
    """ init method is like the constructor """
    def __init__(self, master):
        #super(Application, self).__init__(master) # some docs use this
        Frame.__init__(self, master) # other docs use this
        self.grid()
        self.setup_gui()
        self.setup_picam()

    def setup_gui(self):
        """ setup gui widgets here  """
           
        img = PhotoImage(file = "/home/pi/Desktop/cuteWelcome.gif")
        label1= Label(self, image = img, width=200, height=200).grid(row = 1, column = 0)
        self.image = img

        
        label2 = Label(self,
                      text = "Choose a filter from the drop down menu.", padx = 20, pady = 20).grid(row = 0,
                                                                           column = 1)
        
        self.options = ["default", "cartoon", "pastel"]
        self.var = StringVar()
        self.var.set("")
        self.drop = OptionMenu(self,
                               self.var,
                               *self.options,
                               command = self.dropfunction).grid(row = 1, column = 1, padx = 20, pady=20)

        label3 = Label(self, text = "When you're ready, click the button below.", padx = 10, pady = 10).grid(row = 2,
                                                                           column = 1, padx = 20, pady=20)
        
        button1 = Button(self, text = "Take Picture",
                command = self.button1_event).grid(row = 3, column = 1, padx = 20, pady = 20)

    
    def dropfunction(self, value):
        
        self.filter = value
        if value == "default":
            self.camera.stop_preview()
            self.camera.image_effect = "none"
            self.camera.start_preview()
        else:
            if value == "cartoon":
                self.camera.stop_preview()
                self.camera.image_effect = "cartoon"
                self.camera.start_preview()
            else:
                self.camera.stop_preview()
                self.camera.image_effect = "pastel"
                self.camera.start_preview()
        
       
    def button1_event(self):
        self.wiccamera = WicCamera(self.camera)
        
        if self.filter == "default":
            self.wiccamera.takePicture()
        else:
            if self.filter == "cartoon":
                self.wiccamera.takeCartoon()
            else:
                self.wiccamera.takePastel()

        # added 12/07 s.o
        # sleep then launch another window
        # second window will need to be edited to suit needs
        sleep(1)
        ##self.newWindow = Toplevel(self.master)
        ## to have the 2x2 option window self.app = GUI2(self.newWindow)
        ##open the keyboard window
        self.app = GUIKeyboard()

        
        ##root.destroy()
##
##    def button2_event(self):
##        print("Button 2 pressed")
##        self.camera.stop_preview()
##        self.camera.close()
##        root.destroy()
##
##    def button3_event(self):
##        print("Button 3 pressed")
##        self.camera.stop_preview()
##        self.camera.close()
##        root.destroy()

    def setup_picam(self):
        print("This is where you would start the preview of the camera")
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1080,720)
        self.camera.rotation = 270
        self.camera.hflip = True
        self.camera.preview_fullscreen = False
        self.camera.preview_window = (15,30,330,380)
        self.camera.start_preview()

        self.filter = "default"
        
        
#    def creat_window():
#        window = tk.TopLevel(root)

        


root = Tk()
root.title("GUI Test")
root.geometry("800x380+0+0") # force main frame to be certain size and location
app = MainApplication(root)         # make an object
app.pack()
root.mainloop()
