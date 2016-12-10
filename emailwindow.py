import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


infofile = open("info.txt", "r")
 
fromaddr = infofile.readline() # first line - full gmail from address
password = infofile.readline() # second line - password


#print ("e " + fromaddr)
#print ("p " + password)

def emailMe(self,x)
toaddr = x
subject = "Astronomy Night 2016 Photo Booth"
filename = "collage.jpg"
body = "Here is your collage from the Photo Booth"
path_to_directory = "/home/pi/Desktop/PhotoBooth/"


infofile.close()

msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
 
msg.attach(MIMEText(body, 'plain'))


attachment = open(path_to_directory + filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


print ("done sending email")


