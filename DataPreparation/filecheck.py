#this  file is to see for all the images in the dataset by providing value to no_of_folders and no_of_images
#default no_of_images to use is 10

import cv2
import numpy as np
from IMREAD import read_image
no_of_folders=3
no_of_images=20
for i in range(no_of_folders):
    for j in range(no_of_images):
        img = read_image('data/s' + str(40+i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        cv2.imshow("cropped", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()