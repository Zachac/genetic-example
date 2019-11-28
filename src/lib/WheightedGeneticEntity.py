import random

from lib.GeneticEntity import GeneticEntity

wheights = [0.9, -0.4, -0.8, 0.6, -0.4, 0.1]

class WheightedGeneticEntity(GeneticEntity):
    

    def __init__(self):
        self.genes = []

        for i in range(len(wheights)):
            self.genes.append(random.randint(-1, 1))

    def fitness(self):
        fitness = 0

        for i in range(len(wheights)):
            fitness += wheights[i] * self.genes[i]

        return fitness / len(wheights)

    def mate(self, other):
        """ Return a new instance of this class that is the result
            of mating these two instances """
        raise NotImplementedError("Please Implement this method")
