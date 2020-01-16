import _Model
from ImageProcessing import capture
#take image
#define url and pass to capture_image
_Model.train()

#url=''
#captured_img=capture(url)  
#captured_img=captured_img[::size,::size]
##predict function in here
#
#sum=np.zeros(no_of_folders)
#size=2
#x_match = np.zeros([1,2,1, 56, 46])
#model=Model.train()
##the image to be checked
#x_match[0,0,0,:,:]=captured_img/255
#model=
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