from cv2 import CascadeClassifier

def detect_face(pixels):
    classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
    boxes = classifier.detectMultiScale(pixels)
    
    for box in boxes:
	    x, y, width, height = box
	    x2, y2 = x + width, y + height
	    break
    

    
    return x,y,x2,y2
