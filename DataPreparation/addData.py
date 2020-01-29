import cv2
from ImageProcessing import capture

def add(folder_num,no_of_people,face_num,no_of_faces, url):
    #send url of the camera from outside
    
    for i in range(no_of_people):
        for j in range(no_of_faces):
            img=capture(url)
            cv2.imwrite('data/s'+str(folder_num+i)+'/'+str(face_num+j+1)+'.pgm',img)
    
    return