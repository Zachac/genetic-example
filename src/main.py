#!/usr/bin/python3.7

from lib.WheightedGeneticEntity import WheightedGeneticEntity
from lib.Population import Population

if __name__ == "__main__":
    population = Population(WheightedGeneticEntity)

    for i in range(5):
        print(f"gen{i}", population.stats())
        population.simulateGenerations(1)
        
