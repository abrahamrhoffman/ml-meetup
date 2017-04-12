import numpy as np
import matplotlib.pyplot as plt
#Our training data
X = np.matrix('0 1;1 1')
y = np.matrix('1;0')
#Let's randomly initialize weights
weights = np.matrix(np.random.normal(0, 5, (2,1)))
def sigmoid(x):
    return np.matrix(1.0 / (1.0 + np.exp(-x)))

#run the neural net forward
def run(X, weights):
	return sigmoid(X * weights) #1x2 * 2x2 = 1x1 matrix

#Our cost function
def cost(X, y, weights):
    nn_output = run(X, weights)
    m = X.shape[0] #num training examples, 2
    return np.sum((1/m) * np.square(nn_output - y))

print('Initial Weight: %s\n' % weights)
print('Cost Before Gradient Descent: %s \n' % cost(X, y, weights))
#Gradient Descent
alpha = 0.05 #learning rate
epochs = 12000 #num iterations
for i in range(epochs):
    #Here we calculate the partial derivatives of the cost function for each weight
    costD1 = np.sum(np.multiply((run(X, weights) - y), np.multiply(run(X, weights), (1 - run(X, weights)))))
    costD2 = np.sum(X[:,0] * np.multiply((run(X, weights) - y), np.multiply(run(X, weights), (1 - run(X, weights)))).T)
    weights[0] = weights[0] - alpha * costD1
    weights[1] = weights[1] - alpha * costD2
print('Final Weight: %s\n' % weights)
print('Final Cost: %s \n' % cost(X, y, weights))
print('Result:\n')
print(np.round(run(X, weights)))
print('Expected Result\n')
print(y)
