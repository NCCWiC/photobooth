from picamera import PiCamera
from time import sleep
import time
class WicCamera:
    
    def takePicture(self):
        camera = PiCamera()

        for x in range(0,4):
            camera.start_preview()
            sleep(3)
            camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
            camera.stop_preview()

        camera.close()

    def takeCartoon(self):
        camera = PiCamera()

        camera.image_effect = 'cartoon' 

        for x in range(0,4):
            camera.start_preview()
            sleep(2)
            camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
            camera.stop_preview()

        camera.close()

    def takePastel(self):
        camera = PiCamera()

        camera.image_effect = 'pastel' 

        for x in range(0,4):
            camera.start_preview()
            sleep(2)
            camera.capture('/home/pi/Desktop/image-' + time.strftime("%Y-%m-%d-%H:%M:%S") + '.jpg')
            camera.stop_preview()

        camera.close()
        
    def preview(self):
        camera = PiCamera()
        camera.start_preview(fullscreen=False, window=(800, 300, 300, 300))
        sleep(7)
        camera.stop_preview()
        
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

