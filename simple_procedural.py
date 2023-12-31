'''
Occupany forecast via Markov Chain - 03.2023

'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
import random as rm

# The statespace
states = ["Occupied","Unoccupied"]

# Possible sequences of events
transitionName = [["OO","OU"],["UU","UO"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.4,0.6],[0.7,0.3]]

# Drop error if the sum of singular probabilities exceed 1
if sum(transitionMatrix[0])+sum(transitionMatrix[1]) != 2:
    print("Error: sum of probabilities of transition matrix higher than 1. Please check matrix.")
else: print("Transition matrix is well defined.")


# A function that implements the Markov model to forecast the state/mood.
def occupancy_forecast(days):
    # Choose the starting state
    OcupancyToday = "Occupied"
    print("Start state: " + OcupancyToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    OccupancyList = [OcupancyToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if OcupancyToday == "Occupied":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "OO":
                prob = prob * 0.4
                OccupancyList.append("Occupied")
                pass
            elif change == "OU":
                prob = prob * 0.6
                OcupancyToday = "Unoccupied"
                OccupancyList.append("Unoccupied")

        elif OcupancyToday == "Unoccupied":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "UU":
                prob = prob * 0.7
                OccupancyList.append("Unoccupied")
                pass
            elif change == "UO":
                prob = prob * 0.3
                OcupancyToday = "Occupied"
                OccupancyList.append("Occupied")
        i += 1
    print("Possible states: " + str(OccupancyList))
    print("End state after "+ str(days) + " days: " + OcupancyToday)
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


print('bye')
