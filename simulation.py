from individual import Individual
import random
import sys

class Simulation:

    def __init__(self, sizePopulation:int, hawkPercent:int, resourceAmount:int, hawkCost:int):

        self.sizePopulation = sizePopulation
        self.hawkPercent = hawkPercent
        self.resourceAmount = resourceAmount
        self.hawkCost = hawkCost
        self.encCount = 0

        self.hawkNum = (hawkPercent * sizePopulation) // 100
        self.doveNum = sizePopulation - self.hawkNum

        self.individualList = self.build_individualList()

    def build_individualList(self):

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

            try:

                itemInput = int(input("> "))

            except ValueError:

                print("Please enter an integer. Not a string.")

                continue

            if itemInput == 1:

                self.statDisplay()

            if itemInput == 2:

                self.individualDisplay()

            if itemInput == 3:

                self.sortedByResources()

            if itemInput == 4:

                self.interactSimulate(1000)

            if itemInput == 5:

                self.interactSimulate(10000)

            if itemInput == 6:

                nInput = int(input("Number of interactions: "))

                self.interactSimulate(nInput)

            if itemInput == 7:

                self.interactSimulateStep()

            if itemInput == 8:

                sys.exit()

            else:

                print("Please choose number from 1 to 8.")

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

    def individualDisplay(self):

        livingList = 0

        for individual in self.individualList:

            if individual.getStatus():
                livingList += 1
                print(f"Individual[{individual.getId()}]={individual.getStrategy()}:{individual.getResource()}")

            else:
                print(f"Individual[{individual.getId()}]=DEAD:{individual.getResource()}")

        print(f"Living: {livingList}")

    def sortedByResources(self):

        sortedResource = sorted(self.individualList, key=lambda individual: individual.getResource(), reverse=True)

        for individual in sortedResource:

            if individual.getStatus():

                print(f"{individual.getStrategy()}:{individual.getResource()}")

            else:

                print(f"Individual[{individual.getId()}]=DEAD:{individual.getResource()}")

    def interactSimulate(self, n:int):

            for i in range(n):

                livingList = []

                for individual in self.individualList:

                    if individual.getStatus():
                        livingList.append(individual)

                if len(livingList) < 2:

                    print("Not enough living individuals")

                    break

                individualOne, individualTwo = random.sample(livingList, 2)

                amountOne, amountTwo = self.simulationLogic(individualOne, individualTwo)

                #print(f"{amountOne} and {amountTwo}")

                print(f"Encounter: {i + 1}")

                print(f"Individual {individualOne.getId()}: {individualOne.getStrategy()}")

                print(f"Individual {individualTwo.getId()}: {individualTwo.getStrategy()}")

                print(f"{individualOne.getStrategy()}/{individualTwo.getStrategy()}: {amountOne:+}      {individualTwo.getStrategy()}: {amountTwo:+}")

                if not individualOne.getStatus():

                    print(f"{individualOne.getStrategy()} one has died!")

                if not individualTwo.getStatus():

                    print(f"{individualTwo.getStrategy()} two has died!")

                print(f"Individual {individualOne.getId()}={individualOne.getResource()}      Individual {individualTwo.getId()}={individualTwo.getResource()}")

                print()

    def simulationLogic(self, indOne:Individual, indTwo:Individual):

        if indOne.getStrategy() == "Dove" and indTwo.getStrategy() == "Dove":

            getAmount = self.resourceAmount // 2

            amountOne = amountTwo = getAmount

            indOne.addResource(amountOne)
            indTwo.addResource(amountTwo)

            return amountOne, amountTwo

        if (indOne.getStrategy() == "Hawk" and indTwo.getStrategy() == "Dove"):

            amountOne = self.resourceAmount
            amountTwo = 0

            indOne.addResource(amountOne)
            indTwo.addResource(amountTwo)

            return amountOne, amountTwo

        elif (indOne.getStrategy() == "Dove" and indTwo.getStrategy() == "Hawk"):

            amountOne = 0
            amountTwo = self.resourceAmount

            indOne.addResource(amountOne)
            indTwo.addResource(amountTwo)

            return amountOne, amountTwo

        if indOne.getStrategy() == "Hawk" and indTwo.getStrategy() == "Hawk":

            amountOne = self.resourceAmount - self.hawkCost

            indOne.addResource(amountOne)

            amountTwo = -self.hawkCost

            indTwo.addResource(amountTwo)

            return amountOne, amountTwo

        return 0, 0

    def interactSimulateStep(self):

        i = 0

        while True:

            i += 1

            livingList = []

            for individual in self.individualList:

                if individual.getStatus():

                    livingList.append(individual)

            if len(livingList) < 2:

                print("Not enough living individuals")

                break

            individualOne, individualTwo = random.sample(livingList, 2)

            amountOne, amountTwo = self.simulationLogic(individualOne, individualTwo)

            #print(f"{amountOne} and {amountTwo}")

            print(f"Encounter: {i}")

            print(f"Individual {individualOne.getId()}: {individualOne.getStrategy()}")

            print(f"Individual {individualTwo.getId()}: {individualTwo.getStrategy()}")

            print(f"{individualOne.getStrategy()}/{individualTwo.getStrategy()}: {amountOne:+}      {individualTwo.getStrategy()}: {amountTwo:+}")

            if not individualOne.getStatus():

                print(f"{individualOne.getStrategy()} one has died!")

            if not individualTwo.getStatus():

                print(f"{individualTwo.getStrategy()} two has died!")

            print(

                f"Individual {individualOne.getId()}={individualOne.getResource()}      Individual {individualTwo.getId()}={individualTwo.getResource()}")

            print()

            userInput = input("Press Enter for next step or type stop to return to menu: ").strip().lower()

            if userInput == "stop":

                break


