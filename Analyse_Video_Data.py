#Import the necessary Packages and scripts for this software to run
import cv2
from collections import Counter
from module import findnameoflandmark,findposition
import webbrowser
import socket

webbrowser.open_new_tab("http://192.168.1.253:8080/stream")

# SENDER
ip = "192.168.1.255"
port = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(message) :
   msg = message.encode('UTF-8')
   print(f'Sending {msg} to {ip}:{port}')
   sock.sendto(msg, (ip, port))


#Use CV2 Functionality to create a Video stream and add some values + variables
cap = cv2.VideoCapture(0)
tip=[8,12,16,20]
tipname=[8,12,16,20]
fingers=[]
finger=[]
lastCounter =[]

#Create an infinite loop which will produce the live feed to our desktop and that will count fingers
while True:
     ret, frame = cap.read() 
     
     #Determines the frame size, 640 x 480 offers a nice balance between speed and accurate identification
     frame1 = cv2.resize(frame, (640, 480))
    
    #Below is used to determine location of the joints of the fingers 
     a = findposition(frame1)
     b = findnameoflandmark(frame1)
     
     #Below is a series of If statement that will determine if a finger is up or down and
     if len(b and a)!=0:
        finger=[]
        if a[0][1:] < a[4][1:]: 
           finger.append(1)
          
        else:
           finger.append(0)   
        
        fingers=[] 

        for id in range(0,4):
            if a[tip[id]][2:] < a[tip[id]-2][2:]:
               fingers.append(1)
            else:
               fingers.append(0)

     #Below will print to the terminal the number of fingers that are up or down          
     x=fingers + finger
     c=Counter(x)
         
     #Below shows the current frame to the desktop 
     cv2.imshow("Frame", frame1);
     key = cv2.waitKey(1) & 0xFF
         
     #Below states that if the |s| is press on the keyboard it will stop the system
     if key == ord("s"):
      sendMessage(str(9))
      break    
     
     # Below will send a new count if it is different from the previous 
     # and print the message sent  
     if(c != lastCounter):
         lastCounter = c
         up=c[1]
         down=c[0]

         sendMessage(str(up))




