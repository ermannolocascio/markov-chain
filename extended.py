'''
This example derives from this tutorial: https://www.datacamp.com/tutorial/markov-chains-python-tutorial
Main author Ermanno Lo Cascio 03.2023

Matrix convention:

states = ["Occupied","Unoccupied"]
transitionName = [["OO_0_0_0_0","OU_0_0_0_0"],["UU_0_0_0_0","UO_0_0_0_0"]] ----> "OO Monday, 13.06.2023 h 20.30" = OO_6_2_20_30
transitionMatrix = [ [0.1], [0.2]  ]

'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import random as rm

# The statespace
states = ["Occupied","Unoccupied"]

# Possible sequences of events simple one
transitionName_occ = [["OO_0_0","OU_0_0"], ["OO_0_1","OU_0_1"]]

transitionName_unocc = [["UU_0_0","UO_0_0"], ["UU_0_1","UO_0_1"]]

# Probabilities matrix (transition matrix)
transitionMatrix_occ = [[0.4,0.6], [0.35,0.65]]
transitionMatrix_unocc  = [[0.7,0.3], [0.8,0.2]]

'''
# Drop error if the sum of singular probabilities exceed 1
if sum(transitionMatrix[0])+sum(transitionMatrix[1]) != 2:
    print("Error: sum of probabilities of transition matrix higher than 1. Please check matrix.")
else: print("Transition matrix is well defined.")

'''
# A function that implements the Markov model to forecast the occupancy.
def occupancy_forecast(days):
    # Choose the starting state
    OccupancyToday = "Occupied"
    print("Start state: " + OccupancyToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    OccupancyList = [OccupancyToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if OccupancyToday == "Occupied":
            for n in range(len(transitionName_occ)):
                # assign coherent not random possible change
                change = np.random.choice(transitionName_occ[n], replace=True, p=transitionMatrix_occ[n])

                # Loop through lists elements
                for k in range(len(transitionName_occ)):
                    for j in range(len(transitionName_occ[k])):

                        # When we have a match between change and list item, then pick the transition probability
                        if change == transitionName_occ[k][j] and 'OO' in change:
                            prob = prob * float(transitionMatrix_occ[k][j])
                            OccupancyList.append("Occupied")
                            pass
                        elif change == transitionName_occ[k][j] and 'OU' in change:
                            prob = prob * float(transitionMatrix_occ[k][j])
                            OccupancyToday = "Unoccupied"
                            OccupancyList.append("Unoccupied")

        elif OccupancyToday == "Unoccupied":
            for n in range(len(transitionName_unocc)):
                # assign coherent not random possible change
                change = np.random.choice(transitionName_unocc[n], replace=True, p=transitionMatrix_unocc[n])

                # Loop through lists elements
                for k in range(len(transitionName_unocc)):
                    for j in range(len(transitionName_unocc[k])):

                        # When we have a match between change and list item, then pick the transition probability
                        if change == transitionName_unocc[k][j] and 'UO' in change:
                            prob = prob * float(transitionMatrix_unocc[k][j])
                            OccupancyList.append("Occupied")
                            pass
                        elif change == transitionName_unocc[k][j] and 'UU' in change:
                            prob = prob * float(transitionMatrix_unocc[k][j])
                            OccupancyToday = "Unoccupied"
                            OccupancyList.append("Unoccupied")

        i += 1
    print("Possible states: " + str(OccupancyList))
    print("End state after "+ str(days) + " days: " + OccupancyToday)
    print("Probability of the possible sequence of states: " + str(prob))

    print(days)
    dd = []
    cs = []
    for d, s in zip(range(days), OccupancyList):
        dd.append(d)
        if s == 'Occupied':
            cs.append(1)
        else:
            cs.append(0)

    # make plot
    plt.bar(dd, height=cs)
    plt.show()

# Function that forecasts the possible state for the next x days

occupancy_forecast(7)
