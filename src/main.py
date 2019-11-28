#!/usr/bin/python3.7

from lib.GeneticEntity import GeneticEntity
from lib.Population import Population

if __name__ == "__main__":
    population = Population(GeneticEntity)
    population.simulateGenerations(5)
    print(population.stats())
