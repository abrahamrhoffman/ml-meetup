import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
#Our training data
X = np.matrix('0 1;1 1')
y = np.matrix('1;0')
#Let's randomly initialize weight to 5, just so we can see gradient descent at work

weights = np.matrix(np.random.normal(0,5, (2,1)))

#sigmoid function
def sigmoid(x):
	return np.matrix(1.0 / (1.0 + np.exp(-x)))

#run the neural net forward
def run(X, weights):
	return sigmoid(X * weights) #1x2 * 2x2 = 1x1 matrix

#Our cost function
def cost(X, y, weights):
	nn_output = run(X, weights)
	m = X.shape[0] #num training examples, 2
	return np.sum((1/m) * np.square(nn_output - y)) #MSE
#random pairs of theta1 and theta2 to feed into our cost function
theta1 = np.random.permutation(np.linspace(-15, 15, 500))
theta2 = np.random.permutation(np.linspace(-15, 15, 500))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
zs = [cost(X, y, np.matrix(theta).T) for theta in zip(theta1, theta2)]
ax.plot_trisurf(theta1, theta2, zs, linewidth=.02, cmap=cm.jet)
ax.azim = 160
ax.set_xlabel('Theta1')
ax.set_ylabel('Theta2')
ax.set_zlabel('Cost')
plt.show()
