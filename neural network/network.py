#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kyle Strokes
SL: Sean Current
ISTA 331
Neural Network Final
5/9/2020

This program takes a csv file of seed data and builds a neural network with
Keras. I found that a reliable 0.89 to 0.94 accuracy lies with the parameters:
    
    Network architecture: [150, 80]
    Activation function: tanh
    Number of epochs: 18
    
The first layer having 150 neurons and the hidden having 80. I use the hyperbolic
tangent to fit the model in 18 epochs. I did switch the optimizer from sgd to adam
because it was giving me significantly better results.

The model tries to classify a seed as one of three types. 0,1,2.
"""

import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import random

'''
This function takes no parameters. Loads up 'seeds.csv' and split the data into 50/50
training and testing data sets, as well as preps for compatiability with Keras. The
training and testing x and y lists are returned.
'''
def get_data():
    df = pd.read_csv('seeds.csv')
    random.seed(1)
    training_idx = np.random.choice(len(df),size=105,replace=False)
    training = pd.DataFrame([df.iloc[idx] for idx in training_idx])
    testing = pd.DataFrame([df.iloc[n] for n in range(len(df)) if n not in training_idx])
    trainy = [n-1 for n in training['class']]
    trainy = keras.utils.to_categorical(trainy)
    testy = [n-1 for n in testing['class']]
    testy = keras.utils.to_categorical(testy)
    trainx = training.drop(columns=['class'])
    trainx = trainx.to_numpy()
    testx = testing.drop(columns=['class'])
    testx = testx.to_numpy()
    return trainx, trainy, testx, testy

'''
This function takes in a list of integers representing the numbers of neurons in
each layer and a string representing the activation function. The neural network is 
then contructed based on the length of the integer list. The last layer is 3 neurons
because the seed can only be chosen from a set of 3 types. The model bulit is returned.
'''
def setup_network(integers, act):
    model = Sequential()
    for i in integers:
        model.add(Dense(i,activation=act))
    model.add(Dense(3,activation = 'softmax'))
    #adam > sgd
    model.compile(optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'])
    return model 

'''
The model above is passed in as well as a training input x, training output y, and
the number of epochs, e. The model is trained and none is returned.
'''
def train_network(model, x, y, e):
    model.fit(x,y,batch_size=16,epochs=e)
    
'''
The model is then passed in with testing input testx and testing output testy.
The accuracy is returned.
'''
def test_network(model, testx, testy):
    loss, acc = model.evaluate(testx, testy, batch_size=1)
    return acc

'''
Prints out your results
Get around 0.89-0.94 accuracy
'''
def main():
    loi = [150,80]
    fn = 'tanh'
    e = 18
    trainx, trainy, testx, testy = get_data()
    model = setup_network(loi,fn)
    train_network(model, trainx, trainy, e)
    acc = test_network(model, testx, testy)
    print()
    print('''Network architecture: ''' + str(loi) + '''
          Activation function: ''' + fn + '''
          Number of epochs: ''' + str(e) + '''
          Test accuracy: ''' + str(acc))
    
main()