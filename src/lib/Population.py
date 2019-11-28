
class Population:

    def __init__(self, clazz, survivors=4, childrenPerSurvivor=2):
        self.currentGenerataion = []
        self.childrenPerSurvivor = childrenPerSurvivor
        self.survivors = survivors
        self.clazz = clazz

        for i in range(self.survivors):
            self.currentGenerataion.append(clazz())

        # self.mateGeneration()
    
    def stats(self):
        totalCount = len(self.currentGenerataion)
        totalFitness = 0
        maxFitness = self.currentGenerataion[0].fitness()

        for v in self.currentGenerataion:
            totalFitness += v.fitness()
            if v.fitness() >  maxFitness:
                maxFitness = v.fitness()
        
        return {"avg": totalFitness/totalCount, "max": maxFitness}
        


    def cullGeneration(self):
        """ retain only the top survivors for this generation """
        raise NotImplementedError("Please Implement this method")

    def mateGeneration(self):
        """ mate the survivors randomly based on childrenPerSurvivor """
        raise NotImplementedError("Please Implement this method")

    def simulateGenerations(self, count=5):
        for i in range(count):
            self.cullGeneration()
            self.mateGeneration()
