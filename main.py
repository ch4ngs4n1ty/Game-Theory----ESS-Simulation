"""
file: main.py

"""

import sys
from numpy import double


def main():

    args = sys.argv[1:]

    try:

        if len(args) == 0 | len(args) > 4:

            print("Usage: ./project02 popSize [percentHawks] [resourceAmt] [costHawk-Hawk]", file=sys.stderr)
            sys.exit(1)

        if len(args) < 2:

            hawkPercent = 0.20

        if len(args) < 3:

            resourceAmount = 50

        if len(args) < 4:

            hawkCost =  100

        # size of individuals in total population
        sizePopulation = int(args[1])

        # percentage of Hawks
        hawkPercent = int(args[2])

        # resource amount
        resourceAmount = int(args[3])

        # hawk-hawk interaction cost
        hawkCost = int(args[4])

    except ValueError:

        print("You should use integers for each of the above", file=sys.stderr)

    hawkNum = (hawkPercent * sizePopulation) // 100

    doveNum = sizePopulation - hawkNum


if __name__ == "__main__":
    main()