from picamera import PiCamera
from time import sleep
import time
from subprocess import call
import os

class WicCamera:

  
    def __init__(self, camera):
        self.camera = camera
        self.folder = '/home/pi/Desktop/PhotoBooth/image-'
        self.camera.annotate_text_size = 100
        #self.camera.annotate_background = camera.Color('black')
    def takePicture(self):
        
        print("BG take pic")

        self.camera.annotate_text = 'Get ready!'
        pictures = [None]*4
        for x in range(0,4):
            #self.camera.start_preview(fullscreen=False, window=(800, 300, 300, 300))
            
            sleep(2)
            # added on 12/7 s.o
            # annotation otherwise can't tell when pic is taken
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            self.camera.annotate_text = '' # take off annotation right before
                                           # taking pic so its not in image
            pictures[x] = self.folder + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg'                               
            self.camera.capture(pictures[x])
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            #self.camera.stop_preview()

        ##self.camera.close()
        print("end of take pic")
        sleep(1)
        os.system("montage " + pictures[0] + " " + pictures[1] + " " +  pictures[2] + " " +  pictures[3] + " " + "-geometry +2+2" + " -quality 100" + " montage.jpg")
        self.camera.annotate_text = 'Done Taking pics'

       

    def takeCartoon(self):

        self.camera.image_effect = 'cartoon' 
        print("BG of take Cartoon")
        self.camera.annotate_text = 'Get ready!'

        pictures = [None]*4
        print ("len " + str(len(pictures)))
        
        for x in range(0,4):
            ##camera.start_preview()
            sleep(2)
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            self.camera.annotate_text = '' # take off annotation right before
                                           # taking pic so its not in image
            pictures[x] = self.folder + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg'
            self.camera.capture(pictures[x])
            print(pictures[x])
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            ##camera.stop_preview()

        ##self.camera.close()
        print("end of take Cartoon")
        self.camera.annotate_text = 'Done Taking pics'
       ## call(["montage", pictures[0], pictures[1], pictures[2], pictures[3], "-geometry +2+2", "-quality 100", "montage.jpg"])
        os.system("montage " + pictures[0] + " " + pictures[1] + " " +  pictures[2] + " " +  pictures[3] + " " + "-geometry +2+2" + " -quality 100" + " montage.jpg")
    def takePastel(self):

        self.camera.image_effect = 'pastel' 
        self.camera.annotate_text = 'Get ready!'
        pictures = [None]*4
        for x in range(0,4):
            ##camera.start_preview()
            sleep(2)
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            self.camera.annotate_text = '' # take off annotation right before
                                           # taking pic so its not in image
            pictures[x] = self.folder + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg'                               
            self.camera.capture(pictures[x])
            self.camera.annotate_text = 'Taking pic ' + str(x+1)
            ##camera.stop_preview()
        os.system("montage " + pictures[0] + " " + pictures[1] + " " +  pictures[2] + " " +  pictures[3] + " " + "-geometry +2+2" + " -quality 100" + " montage.jpg")
         ##self.camera.close()
        self.camera.annotate_text = 'Done Taking pics'
        
    def preview(self):
        self.camera.start_preview(fullscreen=False, window=(800, 300, 300, 300))
        self.camera.rotation = 270
        ##self.camera.hflip = True
        ##_______________________Test Area_____________________
        ##camera.start_preview()
        ##camera.image_effect = 'cartoon' 
        ##sleep(10)
        ##camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
        ##camera.stop_preview()

##        camera.rotation = 180
##        camera.start_preview()
##        sleep(2)
##        camera.stop_preview()
##        camera.capture_sequence([
##            '/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg',
##            '/home/pi/Desktop/image-' + time.strftime("-%Y-%m-%d-%H:%M:%S") + '.jpg',
##            ])
            

##        def countdown( num):
##            camera.annotate_text = num
##
##        for i in range(5,0,-1):
##            countdown(str(i))
##            sleep(1)
##
##            camera.annotate_text = 'Say Cheese!'
        ##sleep(1)
##        camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
        
##        camera.close()
        ##_______________________Test Area_____________________


          
        ##Code for changing effects over time + changing anotations up top
        ##----------------------------------------
        ##camera.start_preview()
        ####for effect in camera.IMAGE_EFFECTS:
        ##camera.awb_mode = 'sunlight'
        ##camera.exposure_mode = 'beach'
        ##camera.annotate_text = "Exposure: %s" % 'beach'
        ##sleep(7)
        ##camera.exposure_mode = 'auto'
        ##camera.annotate_text = "Exposure: %s" % 'none'
        ##sleep(7)
        ##camera.exposure_mode = 'fireworks'
        ##camera.annotate_text = "Exposure: %s" % 'fireworks'
        ##sleep(7)

        ##camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
        ##camera.stop_preview()


        ##    Possibly nice effects
        ##    sketch
        ##    cartoon
        ##----------------------------------------


        ##Messy code for a timer. sleep(1) looks like it takes 1sec.
        ##----------------------------------------
        ##camera.start_preview()
        ##camera.rotation = 180
        ##camera.annotate_text = '1'
        ##sleep(1)
        ##camera.annotate_text = '2'
        ##sleep(1)
        ##camera.annotate_text = '3'
        ##sleep(1)
        ##camera.annotate_text = '4'
        ##sleep(1)
        ##camera.annotate_text = '5'
        ##sleep(1)
        ##camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
        ##camera.stop_preview()
        ##----------------------------------------
