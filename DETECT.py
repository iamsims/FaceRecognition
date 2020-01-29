from cv2 import CascadeClassifier

classifier = CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face(pixels):
    bboxes = classifier.detectMultiScale(pixels)
    
    for box in bboxes:
	    x, y, width, height = box
	    x2, y2 = x + width, y + height
	    break
    

    
    return x,y,x2,y2
