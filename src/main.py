#!/usr/bin/python3.7

from lib.WheightedGeneticEntity import WheightedGeneticEntity
from lib.Population import Population

if __name__ == "__main__":
    # population = Population(WheightedGeneticEntity)

    # for i in range(5):
    #     print(f"gen{i}", population.stats())
    #     population.simulateGenerations(1)
    
    x1 = WheightedGeneticEntity()
    x2 = WheightedGeneticEntity()
    c0 = x1.mate(x2)

    print(x1.genes)
    print(x2.genes)
    print(c0.genes)

