import random

from lib.GeneticEntity import GeneticEntity

wheights = [1, -1, -1, 1, -1, 1]

class WheightedGeneticEntity(GeneticEntity):
    

    def __init__(self, genes=None):
        self.genes = genes or []

        for i in range(len(self.genes), len(wheights)):
            self.genes.append(random.uniform(-1, 1))

    def fitness(self):
        fitness = 0

        for i in range(len(wheights)):
            fitness += wheights[i] * self.genes[i]

        return fitness / len(wheights)

    def mate(self, other):
        newGenes = []

        for i in range(len(wheights)):
            selectedGene = None

            if random.getrandbits(1):
                selectedGene = self.genes[i]
            else:
                selectedGene = other.genes[i]

            if random.random() < 0.05:
                selectedGene = random.uniform(-1, 1)

            newGenes.append(selectedGene)

        return WheightedGeneticEntity(genes=newGenes)

