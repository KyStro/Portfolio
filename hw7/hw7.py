#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kyle Strokes
SL: Sean Current
ISTA 331 Hw7
4/27/20

This module takes data on how people hand write numbers 0-9. This data
is in the form of a 70000x724 dataset where the higher the number of any
data point the darker the mark on the hand written. The data is split into
testing and training data. The data is trained in 3 different models. Predictions
are run thorugh each model and a confustion matrix is made for each. The counts are
then made into probabilities and the matrices are plotted as heat maps for all models.
"""
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
mnist = sio.loadmat('mnist-original.mat')
import pandas as pd

'''
This function gets the data from mnist-original.mat. A 
70000 x 784 2D 'X' value is returned and a 70000 labeled 'y'
list is returned also.
'''
def get_data():
    datat = mnist['data'].transpose()
    return datat, mnist['label'][0]


'''
This function takes in the data 'x' and labels 'y'
and splits each into training and testing sets.
First 60000 are training, while the rest are for
testing the model.
'''
def get_train_and_test_sets(x,y): 
    np.random.seed(42)
    testx = x[-10000:]
    testy = y[-10000:]
    trainy = np.random.permutation(y[:-10000])
    np.random.seed(42)
    trainx=np.random.permutation(x[:-10000])
    return trainx, testx, trainy, testy

'''
This function takes in data 'x' and labels 'y' and
a name of the type of model to use:
    
    SGD -> SGDClassifier
    SVM -> SVC
    default is LogisiticRegression
    
The model is then fit with the training data and
returned.
'''
def train_to_data(X, y, name):
    if name == 'SGD':
        model = SGDClassifier(max_iter=200, tol=0.001)
        model.fit(X[:10000], y[:10000])
    elif name == 'SVM':
        model = SVC(kernel='poly')
        model.fit(X[:10000], y[:10000])
    else:
        model = LogisticRegression(multi_class='multinomial', solver = 'lbfgs')
        model.fit(X, y)
    return model
    
'''
This function takes a trained model, testing x list and testing y list.
each x value is predicted using the model and a confusion matrix is made
mapping predicted values against actual values.
'''
def get_confusion_matrix(model, x, y):
    nums = [n for n in range(10)]
    matrix = [[0 for n in nums] for m in nums]
    predicts = list(model.predict(x))

    for i in range(len(predicts)):
        row = int(predicts[i])
        col = int(y[i])
        matrix[col][row] += 1
    matrix = np.array(matrix)
    return matrix

'''
This function takes in the confusion matrix mentioned above and
gives the conditional probabilities of each count.

P(predicted | actual)

A new matrix with these probabilities is returned.
'''
def probability_matrix(cm):
    nums = [n for n in range(10)]
    matrix = [[0 for n in nums] for m in nums]
    for row in range(len(cm)):
        for col in range(len(cm[row])):
            prob = round(cm[row,col]/sum(cm[row]),3)
            matrix[row][col] = prob
    matrix = np.array(matrix)
    return matrix


'''
This function takes 3 different models and plots their confusion
matrices as black squares. The darker the sqaure the higher probability
main() prints out the 3 graphs.
'''
def plot_probability_matrices(p1,p2,p3):
    f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
    ax1.matshow(p1, cmap='Greys')
    ax2.matshow(p2, cmap='Greys')
    ax3.matshow(p3, cmap='Greys')
    ax1.set_title('Linear SVM',pad=18)
    ax2.set_title('Logistic Regression',pad=18)
    ax3.set_title('Polynomial SVM',pad=18)



def main():
    x,y = get_data()
    trainx, testx, trainy, testy = get_train_and_test_sets(x,y)
    sgd_cmat = get_confusion_matrix(train_to_data(trainx,trainy,'SGD'),testx,testy)
    soft_cmat = get_confusion_matrix(train_to_data(trainx,trainy,''),testx,testy)
    svm_cmat = get_confusion_matrix(train_to_data(trainx,trainy,'SVM'),testx,testy)
    plot_probability_matrices(sgd_cmat,soft_cmat,svm_cmat)
    for mod in (('Linear SVM:', probability_matrix(sgd_cmat)),
                ('Logistic Regression:', probability_matrix(soft_cmat)),
                ('Polynomial SVM:', probability_matrix(svm_cmat))):
                    print(*mod, sep = '\n')
    plt.show()

main()
    
    
