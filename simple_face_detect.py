
# Code came from:
# http://delivery.acm.org/10.1145/1770000/1764861/p50-batenkov.pdf?ip=173.234.41.130&id=1764861&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&CFID=715661116&CFTOKEN=54793452&__acm__=1484237326_9a5a37b964b064097ec0b849a29850c5
import sys
import cv2

storage=cv2.CreateMemStorage(0)
image _ scale=1.3
haar _ scale=1.2
min _ neighbors=1
haar _ flags=0
def detect_and_draw(img):
# allocate temporary images
gray=cv2.CreateImage((img.width,img.height),8,1)
 small _ img=cv2.CreateImage((cv2.Round(img.width/
image _ scale),
 cv2.Round(img.height/image _ scale)), 8, 1 )
# convert color input image to grayscale
cv2.CvtColor( img, gray, cv2.CV _ BGR2GRAY )
# scale input image for faster processing
cv2.Resize( gray, small _ img, cv2.CV _ INTER _ NN )
cv2.EqualizeHist( small _ img, small _ img )
# start detection
if( cascade ):
 faces=cv2.HaarDetectObjects( small _ img,
 cascade, storage,
 haar _ scale, min _ neighbors, haar _ flags )
if faces:
 for (x,y,w,h),n in faces:
 # the input to cv2HaarDetectObjects was resized, so scale the
 # bounding box of each face and convert it to two CvPoints
 pt1=(int(x*image _ scale),int(y*image _ scale))
 pt2=(int((x+w)*image _ scale),
 int((y+h)*image _ scale))
 # Draw the rectangle on the image
 cv2.Rectangle(img,pt1,pt2,cv2.CV _ RGB(255,0,0),3,8,0)
 cv2.ShowImage( “result”, img )
if _ _ name _ _ ==‘ _ _ main _ _ ’:
# Load the Haar cascade
cascade _ name=“./haarcascade _ frontalface
alt _ tree.xml”
cascade=cv2.Load(cascade _ name)
# Start capturing.Can change index if more than one
camera present
capture=cv2.CaptureFromCAM(0)
# Create the output window
cv2.NamedWindow(“result”,1)
frame _ copy=None
while True:
 frame=cv2.QueryFrame( capture )
 # make a copy of the captured frame
 if not frame _ copy:
 frame _ copy=cv2.CreateImage((frame.
 width,frame.height),
 cv2.IPL _ DEPTH _ 8U, frame.nChannels )
 cv2.Copy( frame, frame _ copy )
 detect _ and _ draw(frame _ copy)
 c=cv2.WaitKey(7)
 if c==27: # Escape pressed
 break