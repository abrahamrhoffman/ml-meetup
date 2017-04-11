#!/usr/bin/python
# -*- coding: utf-8 -*-
#######################################
# A Simple NN for MNIST in Tensorflow #
#######################################
# Author : Abe Hoffman #
# Date   : Apr 2017    #
########################

### Required Libraries ###
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3' # Suppress unneeded Tensorflow output. Comment this line to view it again.
import numpy as np
import random as ran

### Tensorflow Imports ###
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data    # Yet another way to download, decompress and import our data into python
mnist = input_data.read_data_sets('MNIST_data', one_hot=True) # See Model Output layer example below for "one_hot" explanation

### Define Functions ###
def train_size(num):
    x_train = mnist.train.images[:num,:] # A selection of "num" sized training images as row vectors.
    y_train = mnist.train.labels[:num,:] # A selection of "num" sized training labels as row vectors.
    return x_train, y_train              # Return both selections

def test_size(num):
    x_test = mnist.test.images[:num,:]   # A selection of "num" sized testing images as row vectors.
    y_test = mnist.test.labels[:num,:]   # A selection of "num" sized testing labels as row vectors.
    return x_test, y_test                # Return both selections

def model():
    ## Define our Model Now
    #
    # This first model will only be two layers:
    # 1. Input layer - Vectors of size 1x784
    # 2. Output layer - Vectors of size 1x10
    #
    # Example Output Vector:
    #         0 1 2 3 4 5 6 7 8 9
    #       [ 0 0 0 0 0 0 0 1 0 0 ]
    #
    # This is called "one-hot" encoding and means that one of our
    # output layer neurons has a "1" in the row/column indicating
    # its proper classification. "7" in the example above.
    #
    # Again, let's say our input image is a "7".
    # - Compute synapse weight and bias (input layer) -> (output layer)
    # - Compute the amount of error between what was predicted and the intended class
    # - Update the weights to get the prediction closer to the required output

    sess = tf.Session() # Start a Tensorflow Session

    x = tf.placeholder(tf.float32, shape=[None, 784]) # Set a placeholder for our input row vectors. None means 784 by any size.
    y_ = tf.placeholder(tf.float32, shape=[None, 10]) # Set a placeholder for our output row vectors. None means 10 by any size.
    W = tf.Variable(tf.zeros([784,10]))               # Initialize our weights of size 784 x 10 to "0". 784 values for each of the 10 classes.
                                                      # - That makes sense right? Every class is going to have 784 pixel intensities.
    b = tf.Variable(tf.zeros([10]))                   # Initialize our biases of 10 to zero. One bias for each output neuron.
                                                      # - For our purposes here, bias is just another minor number that is part of the neuron.
    y = tf.nn.softmax(tf.matmul(x,W) + b)             # Compute (vector(x) times vector(W) plus bias) matrix of (training images by classes) size.
                                                      # - This "y" variable determines the computation size of our training.

    x_train, y_train = train_size(50000)              # Grab a selection of images and labels from our training data
    x_test, y_test = test_size(10000)                 # Grab a selection of images and labels from our testing data

    LEARNING_RATE = 0.1                               # How fast do we want our Neural Network to learn?
                                                      # - Don't set this too high or low, or you will never find the global minimum. A good range is between -1 and 1.
    TRAIN_STEPS = 2500                                # How many epochs should our training loop run for?
                                                      # - Play around with this number until you have obtained the same loss for ~1000 training steps

    # Define our Cost Function. Instead of Residual Sum of Squares, we use "Cross Entropy"
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
        # - This function is taking the log of all our predictions y (whose values range from 0 to 1)
        #   then, it performs element-wise multiplication by the example’s true value y_.
        #   If the log function for each value is close to zero, it will make the value a large negative number (i.e., -np.log(0.01) = 4.6)
        #   If the log function for each value of is close to 1, it will make the value a small negative number (i.e., -np.log(0.99) = 0.1)
        #
        #   Essentially, this cost function is heavily penalizing vetor elements that are further away from the proper result.
        #   If the result is closer to what it is supposed to be, "Cross Entropy" won't penalize as hard.

    init = tf.global_variables_initializer() # Initialize all Global Variables (Requires Tensorflow v1.0 and above)
    sess.run(init)                           # Start the session with all variables initialized

    training = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cross_entropy)  # Perform Gradient Descent at "LEARNING_RATE" speed and minimize our cost function "Cross Entropy".
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))                       # We want our network to predict the labels we pass it! This tells it to do it.
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))                   # Run "accuracy" to classify the unseen data in x_test by comparing its y and y_test.
                                                                                         # - So the model just ran some data through it. How does the newly trained run do on our test data?

    # Start Training on the Training and Testing Data we specified above.
    for i in range(TRAIN_STEPS+1):
        sess.run(training, feed_dict={x: x_train, y_: y_train}) # Feed in "training" (see variable above) and our x_train, y_train images and labels
        if i%100 == 0:                                          # Every 100 Training Steps, print the below.
            print('Training Step:' + str(i) + '  Accuracy =  ' + str(sess.run(accuracy, feed_dict={x: x_test, y_: y_test})) + '  Loss = ' + str(sess.run(cross_entropy, {x: x_train, y_: y_train})))

### Main Function ###
def main():
    model()

if __name__ == "__main__":
    main()

