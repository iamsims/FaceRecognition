from Dependencies.ImageProcessing import capture
import pickle
import numpy as np
from Dependencies.IMREAD import read_image

import serial
ser=serial.Serial('COM3',9600)

modelfile = 'models/final_prediction_new.pickle'
model = pickle.load(open(modelfile, 'rb'))

no_of_folders=9
no_of_images=10
size=2
url='http://10.100.60.253:8080/shot.jpg?rnd=9200110'

print('Active')

while 1:
    x_match = np.zeros([1,2,1, 56, 46])
    sum=np.zeros(no_of_folders)

    while 1:
        a=ser.readline()
        b=str(a)
        response=int(b[2])
        if (response):
            break
    print('Responded by ultrasensor')

    try:
        img=capture(url)
       # img = read_image('authorized_person/' + str(1) + '/' + str(1) + '.pgm', 'rw+')
        img = img[::size, ::size]/255
        x_match[0,1,0,:,:]=img

        for i in range(no_of_folders):
            for j in range(no_of_images):
                img = read_image('authorized_person/' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
                img = img[::size, ::size]/255
                x_match[0,0,0,:,:]=img
                pred=model.predict([x_match[:,0],x_match[:,1]])

                sum[i]+=pred

            sum[i]=sum[i]/no_of_images

        ind = np.argmin(sum)

        if(sum[ind]<0.5):
            val='1'
        ##the one with minimum avg value is  the recognized person and allowed to enter
        else:
            val='0'

        print(sum)
        print(ind+1)
    
    except:
        print('No face in the screen')
        val='0'

    ser.write(val.encode())
        
print('Door lock turned off')