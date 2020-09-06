from Dependencies.ImageProcessing import capture
import pickle
import numpy as np
from Dependencies.IMREAD import read_image

modelfile = 'models/prediction.pickle'
model = pickle.load(open(modelfile, 'rb'))

no_of_folders=9
no_of_images=10
size=2

x_match = np.zeros([1,2,1, 56, 46])
sum=np.zeros(no_of_folders)

#url='http://10.100.20.25:8080/shot.jpg?rnd=9200110'
#img=capture(url)  

img = read_image('authorized_person/s' + str(9) + '/' + str(1) + '.pgm', 'rw+')
img = img[::size, ::size]/255
x_match[0,1,0,:,:]=img

for i in range(no_of_folders):
    for j in range(no_of_images):
        img = read_image('authorized_person/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
        img = img[::size, ::size]/255
        x_match[0,0,0,:,:]=img
        pred=model.predict([x_match[:,0],x_match[:,1]])
       
        sum[i]+=pred
        
    sum[i]=sum[i]/no_of_images

ind = np.argmin(sum)
print(sum)
print('The predicted person is '+ str(ind+1) + ' and the difference from the 9th person is:'+str(sum[ind]))