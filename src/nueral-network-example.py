#!/usr/bin/python3.7
from lib.NueralNetwork import NeuralNetwork

if __name__ == "__main__":
    nn = NeuralNetwork([3, 5, 2], 0)
    print(nn.run([1, 2, 3]))

