"""
file: main.py

"""

import sys
from simulation import Simulation

def main():

    args = sys.argv[1:]

    print(args)

    try:

        if len(args) == 0 | len(args) > 4:

            print("Usage: ./project02 popSize [percentHawks] [resourceAmt] [costHawk-Hawk]", file=sys.stderr)
            sys.exit(1)

        if len(args) > 1:

            # percentage of Hawks
            hawkPercent = int(args[1])

        else:

            hawkPercent = 20

        if len(args) > 2:

            # resource amount
            resourceAmount = int(args[2])

        else:

            resourceAmount = 50

        if len(args) > 3:

            # hawk-hawk interaction cost
            hawkCost = int(args[3])

        else:

            hawkCost =  10

        # size of individuals in total population
        sizePopulation = int(args[0])

        sim = Simulation(sizePopulation, hawkPercent, resourceAmount, hawkCost)
        sim.menu()

    except ValueError:

        print("You should use integers for each of the above", file=sys.stderr)

if __name__ == "__main__":
    main()