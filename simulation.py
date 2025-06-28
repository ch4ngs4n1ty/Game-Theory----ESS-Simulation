from individual import Individual
import random


class Simulation:

    def __init__(self, sizePopulation:int, hawkPercent:int, resourceAmount:int, hawkCost:int):

        self.sizePopulation = sizePopulation
        self.hawkPercent = hawkPercent
        self.resourceAmount = resourceAmount
        self.hawkCost = hawkCost
        self.encCount = 0

        self.hawkNum = (hawkPercent * sizePopulation) // 100
        self.doveNum = sizePopulation - self.hawkNum

        self.individualList = self.individualList()

    def individualList(self):

        individual = []

        # Constructor for Individual class is ((self, id:int, strategy:str, resource:int = 0, status:bool = True)

        for i in range(self.sizePopulation):

            if i < self.hawkNum:
                individual.append(Individual(i, "Hawk"))  #i = id and hawk = strategy, others set with default
            else:
                individual.append(Individual(i, "Dove")) #i = id and dove = strategy, others set with default

        return individual



    def menu(self):

        print("===============MENU=============\n")
        print("1 ) Starting Stats\n")
        print("2 ) Display Individuals and Points\n")
        print("3 ) Display Sorted\n")
        print("4 ) Have 1000 interactions\n")
        print("5 ) Have 10000 interactions\n")
        print("6 ) Have N interactions\n")
        print("7 ) Step through interactions " + "Stop" + " to return to menu\n")
        print("8 ) Quit\n")
        print("================================\n")





