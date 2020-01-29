from IMREAD import read_image
import numpy as np
import pickle

def get_data(size,no_of_folders,no_of_faces,total_sample_size):
    #read the image
    total_no_of_faces=int(no_of_faces.sum())
    image = read_image('dataNew/s' + str(1) + '/' + str(1) + '.pgm', 'rw+')
    
    #reduce the size
    image = image[::size, ::size]
    
    #get the new size
    dim1 = image.shape[0]
    dim2 = image.shape[1]
    
    count = 0
    
    #initialize the numpy array with the shape of [total_sample, no_of_pairs, dim1, dim2]
    x_geuine_pair = np.zeros([total_sample_size, 2, 1, dim1, dim2])  # 2 is for pairs
    y_genuine = np.zeros([total_sample_size, 1])
    
    for i in range(no_of_folders):
        for j in range(int(total_sample_size/no_of_folders)):
            ind1 = 0
            ind2 = 0
            
            #read images from same directory (genuine pair)
            while ind1 == ind2:
                ind1 = np.random.randint(int(no_of_faces[i]))
                ind2 = np.random.randint(int(no_of_faces[i]))
            
            # read the two images
            img1 = read_image('dataNew/s' + str(i+1) + '/' + str(ind1 + 1) + '.pgm', 'rw+')
            img2 = read_image('dataNew/s' + str(i+1) + '/' + str(ind2 + 1) + '.pgm', 'rw+')
            
            #reduce the size
            img1 = img1[::size, ::size]
            img2 = img2[::size, ::size]
            x_geuine_pair[count, 0, 0, :, :] = img1
            x_geuine_pair[count, 1, 0, :, :] = img2
            
            #as we are drawing images from the same directory we assign label as 1. (genuine pair)
            y_genuine[count] = 1
            count += 1

    count = 0
    x_imposite_pair = np.zeros([total_sample_size, 2, 1, dim1, dim2])
    y_imposite = np.zeros([total_sample_size, 1])
    
    for i in range(int(25*no_of_folders)):#25*no_of_folders=total_sample_size/no_of_faces
        face_num=int(no_of_faces[int(i/25)])
        for j in range(face_num):
            
            #read images from different directory (imposite pair)
            while True:
                ind1 = np.random.randint(no_of_folders)
                ind2 = np.random.randint(no_of_folders)
                if ind1 != ind2:
                    break

            j=np.random.randint(int(no_of_faces[ind1]))
            k=np.random.randint(int(no_of_faces[ind2]))
                    
            img1 = read_image('dataNew/s' + str(ind1+1) + '/' + str(j + 1) + '.pgm', 'rw+')
            img2 = read_image('dataNew/s' + str(ind2+1) + '/' + str(k + 1) + '.pgm', 'rw+')

            img1 = img1[::size, ::size]
            img2 = img2[::size, ::size]
            

            x_imposite_pair[count, 0, 0, :, :] = img1
            x_imposite_pair[count, 1, 0, :, :] = img2
            #as we are drawing images from the different directory we assign label as 0. (imposite pair)
            y_imposite[count] = 0
            count += 1
            
    #now, concatenate, genuine pairs and imposite pair to get the whole data
    X = np.concatenate([x_geuine_pair, x_imposite_pair], axis=0)/255
    X.shape   
    Y = np.concatenate([y_genuine, y_imposite], axis=0)
    return X, Y

with open("imageperfolderaftercontrol.txt", "rb") as fp:   # Unpickling
    no_of_faces = pickle.load(fp)

size = 2
sample_factor=25
no_of_folders=no_of_faces.size
print(no_of_folders)
print(no_of_faces.sum())
total_sample_size=int((no_of_faces.sum())*sample_factor)
print(total_sample_size)
#X, Y =get_data(size,no_of_folders,no_of_faces, total_sample_size)
