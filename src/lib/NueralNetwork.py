import numpy as np

from scipy.special import expit as activation_function
from scipy.stats import truncnorm

""" from https://www.python-course.eu/neural_networks_with_python_numpy.php """
def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

class NeuralNetwork:
    
    """ layers: list of how many nodes for each layer, layer0 is the input node 
        learning_rate: ???
    """
    def __init__(self, layers, learning_rate):
        self.layers = layers
        self.learning_rate = learning_rate
        self.weights = []

        # layer0 is input layer and has no weights
        self.weights.append(None)

        # calculate random weights for subsequent layers
        for i in range(1, len(layers)):
            max_range = 1 / np.sqrt(self.layers[i - 1])
            layer_weights = truncated_normal(low=-max_range, upp=max_range)
            self.weights.append(layer_weights.rvs((self.layers[i], self.layers[i - 1])))

    def train(self):
        pass
    
    def run(self, input):
        # format from horizontal matrix to vertical matrix
        input = np.array(input, ndmin=2).T

        for i in range(1, len(self.weights)):
            output = np.dot(self.weights[i], input)
            input = activation_function(output)

        return input
