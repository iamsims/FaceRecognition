#API req so that it doesn't comppile everytime i run the program 
from sklearn.model_selection import train_test_split
from keras import backend as K
from keras.layers import Activation
from keras.layers import Input, Lambda, Dense, Dropout, Convolution2D, MaxPooling2D, Flatten
from keras.models import Sequential, Model
from keras.optimizers import RMSprop
import datasetprep

initial_no_of_folders=43
initial_no_of_faces=10
size = 2
sample_factor=25

#no_of_faces,total_sample_size=datasetprep.augment_dataset(initial_no_of_folders,initial_no_of_faces,sample_factor)

X, Y = datasetprep.get_data(size,initial_no_of_folders,no_of_faces, total_sample_size)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=.25)


def build_base_network(input_shape):
    
    seq = Sequential()
    
    nb_filter = [6, 12]
    kernel_size = 3
    
    
    #convolutional layer 1
    seq.add(Convolution2D(nb_filter[0], kernel_size, kernel_size, input_shape=input_shape,
                          border_mode='valid', dim_ordering='th'))
    seq.add(Activation('relu'))
    seq.add(MaxPooling2D(pool_size=(2, 2)))  
    seq.add(Dropout(.25))
    
    #convolutional layer 2
    seq.add(Convolution2D(nb_filter[1], kernel_size, kernel_size, border_mode='valid', dim_ordering='th'))
    seq.add(Activation('relu'))
    seq.add(MaxPooling2D(pool_size=(2, 2), dim_ordering='th')) 
    seq.add(Dropout(.25))

    #flatten 
    seq.add(Flatten())
    seq.add(Dense(128, activation='relu'))
    seq.add(Dropout(0.1))
    seq.add(Dense(50, activation='relu'))
    return seq

def euclidean_distance(vects):
    x, y = vects
    return K.sqrt(K.sum(K.square(x - y), axis=1, keepdims=True))

def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)

def contrastive_loss(y_true, y_pred):
        margin = 1
        return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))

def compute_accuracy(predictions, labels):
    return labels[predictions.ravel() < 0.5].mean()

def train():
    input_dim = x_train.shape[2:]
    img_a = Input(shape=input_dim)
    img_b = Input(shape=input_dim)

    base_network = build_base_network(input_dim)
    feat_vecs_a = base_network(img_a)
    feat_vecs_b = base_network(img_b)

    distance = Lambda(euclidean_distance, output_shape=eucl_dist_output_shape)([feat_vecs_a, feat_vecs_b])

    epochs = 13
    rms = RMSprop()

    model = Model(input=[img_a, img_b], output=distance)

    model.compile(loss=contrastive_loss, optimizer=rms)

    img_1 = x_train[:, 0]
    img_2 = x_train[:, 1]

    model.fit([img_1, img_2], y_train, validation_split=.25,
              batch_size=128, verbose=2, nb_epoch=epochs)

    pred = model.predict([x_test[:, 0], x_test[:, 1]])
    print(compute_accuracy(pred, y_test))
    return model

