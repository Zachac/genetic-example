

class GeneticEntity:
    
    def fitness(self):
        """ Evaluates the fitness of this creature """
        raise NotImplementedError("Please Implement this method")

    def mate(self, other):
        """ Return a new instance of this class that is the result
            of mating these two instances """
        raise NotImplementedError("Please Implement this method")

    def __lt__(self, other):
        return self.fitness() < other.fitness()
