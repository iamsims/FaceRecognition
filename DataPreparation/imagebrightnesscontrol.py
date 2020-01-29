import cv2
import numpy as np
from IMREAD import read_image
import pickle

no_of_folders=45;
no_of_images=10;
contrast_control=[1,2,3]#(1-3)
brightness_control=[0,10,20,30,40,50,60,70,80,90,100]#0-100
file_num=np.zeros(no_of_folders)
print(file_num)

for i in range(no_of_folders):
    distance=0
    for j in range(no_of_images):
        img = read_image('data/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        for contrast in contrast_control:
            for brightness in brightness_control:
                new_img=img*contrast+brightness
                if(new_img.min()==0 or new_img.max()>254):
                    break;
                cv2.imwrite('dataNew/s'+str(i+1)+'/'+str(distance+1)+'.pgm',new_img)
                #if(i>40):
                #cv2.imshow("cropped", new_img)
                #cv2.waitKey(0)
                #cv2.destroyAllWindows()
                file_num[i]+=1
                distance+=1


with open("imageperfolderaftercontrol.txt", "wb") as fp:   #Pickling
  pickle.dump(file_num, fp)
with open("imageperfolderaftercontrol.txt", "rb") as fp:   # Unpickling
  b = pickle.load(fp)

#total_image*25
#total_no_of_images=brightnessAndContrastControl(no_of_folders,20)
