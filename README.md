# Markov Chain Python

**Python Example of Markov Chain with 1 Agent**

In this simple example, a Markov Chain is implemented considering 1 agent. The term "agent" in this example refers to the number of people in the zone.

This code enables the stochastic simulation of occupancy in a specific zone based on the probabilities set in the transition matrix. The core of the code lies in the `np.random.choice()` function, which is used to generate a pseudo-random number conditioned by the probabilities.

There are two versions of the same code: `simple_procedural.py` and `extended.py`. The latter is simply a parameterized version of the former that loops through the length of the transition matrix to pick the corresponding value.
