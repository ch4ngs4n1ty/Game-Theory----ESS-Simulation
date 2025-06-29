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

        while True:

            print("===============MENU=============")
            print("1 ) Starting Stats")
            print("2 ) Display Individuals and Points")
            print("3 ) Display Sorted")
            print("4 ) Have 1000 interactions")
            print("5 ) Have 10000 interactions")
            print("6 ) Have N interactions")
            print("7 ) Step through interactions " + "Stop" + " to return to menu")
            print("8 ) Quit")
            print("================================")

            inputNum = int(input(">"))

            if inputNum == 1:

                self.statDisplay()

    def statDisplay(self):

        print(f"Population size: {self.sizePopulation}")
        print(f"Percentage of Hawks: {self.hawkPercent}%")
        print(f"Number of Hawks: {self.hawkNum}")
        print()
        print(f"Percentage of Doves: {(self.doveNum / self.sizePopulation) * 100:.0f}%")
        print(f"Number of Doves: {self.doveNum}")
        print()
        print(f"Each resource is worth: {self.resourceAmount}")
        print(f"Cost of Hawk-Hawk interaction: {self.hawkCost}")








