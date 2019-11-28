#!/usr/bin/python3.7

from lib.WheightedGeneticEntity import WheightedGeneticEntity
from lib.Population import Population

if __name__ == "__main__":
    population = Population(WheightedGeneticEntity, survivors=8, childrenPerSurvivor=24)
    
    for i in range(100):
        if i <= 10 or i % 10 == 0:
            print(f"gen{i}", population.stats())
        population.simulateGenerations(1)
    
    
    print("final", population.stats())
