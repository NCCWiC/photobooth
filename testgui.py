from tkinter import *
import os
from camera import WicCamera
import _thread
import time

class MainApplication(Frame):
    
    """ init method is like the constructor """
    def __init__(self, master):
        #super(Application, self).__init__(master) # some docs use this
        Frame.__init__(self, master) # other docs use this
        self.grid()
        self.setup_gui()
        

    def setup_gui(self):
        """ setup gui widgets here  """
        Button( self,
                text = "Button1",
                command = self.button1_event
                ).grid(row=0, column = 0)

        
        Label(self, text = "Sample Text").grid(row = 0, column = 1)

    def button1_event(self):
        cam=WicCamera()
        cam.preview()
        print("Button 1 pressed")

    def setup_picam(self):
        cam=WicCamera()
        cam.preview()


# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

root = Tk()                             
root.title("GUI Test")
#root.geometry("300x280+800+300") # force main frame to be certain size and location
app = MainApplication(root)# make an object
try:
    _thread.start_new_thread(app.setup_picam)
    #_thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
    print ("Error: unable to start thread")
root.mainloop()
