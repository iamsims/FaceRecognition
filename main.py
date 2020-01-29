from ImageProcessing import capture
import pickle
import numpy as np
from IMREAD import read_image

modelfile = 'models/final_prediction_new.pickle'
print('here')
model = pickle.load(open(modelfile, 'rb'))

no_of_folders=9
no_of_images=10
size=2

x_match = np.zeros([1,2,1, 56, 46])
sum=np.zeros(no_of_folders)

url='http://10.100.20.25:8080/shot.jpg?rnd=9200110'
captured_img=capture(url)  
captured_img=captured_img[::size,::size]
x_match[0,0,0,:,:]=captured_img/255

for i in range(no_of_folders):
    for j in range(no_of_images):
        img = read_image('authorized_person/' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        img = img[::size, ::size]/255
        x_match[0,1,0,:,:]=img
        pred=model.predict([x_match[:,0],x_match[:,1]])
       
        sum[i]+=pred
        
    sum[i]=sum[i]/10
           
ind = np.argmin(sum)

if(sum[ind]<0.5):
    val='1'
##the one with minimum avg value is  the recognized person and allowed to enter
else:
    val='0'

print(sum)
print(sum[ind])

#img = read_image('authorized_person/' + str(9) + '/' + str(1) + '.pgm', 'rw+')
#img = img[::size, ::size]/255
#x_match[0,1,0,:,:]=img
#for i in range(no_of_folders):
#    for j in range(no_of_images):
#        img = read_image('authorized_person/' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
#        img = img[::size, ::size]/255
#        x_match[0,0,0,:,:]=img
#        pred=model.predict([x_match[:,0],x_match[:,1]])
#       
#        sum[i]+=pred
#        
#    sum[i]=sum[i]/10


ser.write(val.encode())