#from ImageProcessing import capture
import pickle
import numpy as np
from IMREAD import read_image
#def contrastive_loss(y_true, y_pred):
#        margin = 1
#        return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))
#from keras.models import load_model

#take image
#define url and pass to capture_image
#load pickle file

modelfile = 'models/final_prediction.pickle'
print('here')
model = pickle.load(open(modelfile, 'rb'))
#model = load_model(modelfile, custom_objects={'contrastive_loss':                   
#contrastive_loss})

print('I am here')
#url=''
#captured_img=capture(url)  
#captured_img=captured_img[::size,::size]
#predict function in here

no_of_folders=43
sum=np.zeros(no_of_folders)
size=2
x_match = np.zeros([1,2,1, 56, 46])
#the image to be checked
img = read_image('data/s' + str(1) + '/' + str(1) + '.pgm', 'rw+')
img = img[::size, ::size]/255
x_match[0,0,0,:,:]=img

img = read_image('data/s' + str(1)+ '/' + str(2) + '.pgm', 'rw+')
img = img[::size, ::size]/255
x_match[0,1,0,:,:]=img
print('I reached here ')
pred=model.predict([x_match[:,0],x_match[:,1]])
print(pred)




#for i in range(no_of_folders):
#    for j in range(no_of_images):
#        img = read_image('data/s' + str(i+1) + '/' + str(j+1) + '.pgm', 'rw+')
#        img = img[::size, ::size]/255
#        x_match[0,1,0,:,:]=img
#        pred=model.predict([x_match[:,0],x_match[:,1]])
#       # if (pred>0.5) :
#       #     pred=1
#       # else:
#       #     pred=0
#        sum[i]+=pred
#        
#    sum[i]=sum[i]/10
#            
#ind = np.argmin(sum)
#if(ind>0.5):
#    print("the person is "+str(ind+1))
##the one with minimum avg value is  the recognized person and allowed to enter
#else:
#    print("Intruder alert")
#
#print(sum)
#