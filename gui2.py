from tkinter import *
#from gui3 import GUI3

# added 12/07 s.o
## change this GUI to what you need


class GUI2(Frame):
    
    """ init method is like the constructor """
    def __init__(self, master):
        #super(Application, self).__init__(master) # some docs use this
        Frame.__init__(self, master) # other docs use this
        self.grid()
        self.setup_gui()
 #       self.setup_picam()

    def setup_gui(self):
        """ setup gui widgets here  """
        Button( self,
                text = "Button in window 2",
                command = self.button1_event
                ).grid(row=0, column = 0)

        
        Label(self, text = "Sample Text 2").grid(row = 0, column = 1)

    def button1_event(self):
        print("Button 1 pressed in window 2")
        self.newWindow3 = Toplevel(self.master)
        self.app3 = GUI3(self.newWindow3)
        #self.master.destroy()

#    def setup_picam(self):
#        print("This is where you would start the preview of the camera")












		
