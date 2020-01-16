from ImageProcessing import capture

import pickle
import numpy as np
from IMREAD import read_image

modelfile = 'models/final_prediction.pickle'
print('here')
model = pickle.load(open(modelfile, 'rb'))


no_of_folders=43
no_of_images=20
size=2

x_match = np.zeros([1,2,1, 56, 46])
sum=np.zeros(no_of_folders)

url='http://10.100.61.234:8080/shot.jpg?rnd=793248'
captured_img=capture(url)  
captured_img=captured_img[::size,::size]
x_match[0,0,0,:,:]=captured_img/255

for i in range(no_of_folders):
    for j in range(no_of_images):
        img = read_image('data/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        img = img[::size, ::size]/255
        x_match[0,1,0,:,:]=img
        pred=model.predict([x_match[:,0],x_match[:,1]])
       # if (pred>0.5) :
       #     pred=1
       # else:
       #     pred=0
        sum[i]+=pred
        
    sum[i]=sum[i]/20
            
ind = np.argmin(sum)
if(ind>0.5):
    print("the person is "+str(ind+1))
#the one with minimum avg value is  the recognized person and allowed to enter
else:
    print("Intruder alert")

print(sum)