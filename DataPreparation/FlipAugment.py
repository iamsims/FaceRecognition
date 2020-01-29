#this file was run to use 

import cv2
import numpy as np
from IMREAD import read_image
import pickle

with open("imageperfolderaftercontrol.txt", "rb") as fp:   # Unpickling
    b = pickle.load(fp)

no_of_folders=b.size
no_of_faces=b

#has to be run only once for flipping of data
def flipping(no_of_folders,no_of_faces):
    for i in range(no_of_folders):
        face_num=int(no_of_faces[i])
        for j in range(face_num):
            img = read_image('dataNew/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
            flipHorizontal = cv2.flip(img,1)
            cv2.imwrite('dataNew/s'+str(i+1)+'/'+str(face_num+j+1)+'.pgm',flipHorizontal)
            #augmented in the same folder
    
    return 2*no_of_faces

final_no_of_faces= flipping(no_of_folders,no_of_faces)
print(final_no_of_faces)
print(final_no_of_faces.sum())

with open("imageperfolderaftercontrolandflipping.txt", "wb") as fp:   #Pickling
  pickle.dump(final_no_of_faces, fp)
