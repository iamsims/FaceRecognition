import cv2
import numpy as np
from IMREAD import read_image
import pickle


no_of_folders=2;
no_of_images=20;
contrast_control=[1,2,3]#(1-3)
brightness_control=[0,10,20,30,40,50,60,70,80,90,100]#0-100
distance=0;
file_num=np.zeros(no_of_folders)


for i in range(no_of_folders):
    distance=0
    for j in range(no_of_images):
        img = read_image('data/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        for contrast in contrast_control:
            for brightness in brightness_control:
                new_img=img*contrast+brightness
                if(new_img.min()==0 or new_img.max()>254):
                    break;
                cv2.imwrite('dataNew/s'+str(i+1)+'/'+str(distance+j+1)+'.pgm',new_img)
                cv2.imshow("cropped", new_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                file_num[i]+=1
                distance+=1

with open("imageperfolder.txt", "wb") as fp:   #Pickling
  pickle.dump(file_num, fp)

with open("imageperfolder.txt", "rb") as fp:   # Unpickling
  b = pickle.load(fp)

print(b)