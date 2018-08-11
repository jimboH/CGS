# Google Summer of Code 2018 Report

## Achievements  
This year, I worked on the project Contextual Geometric Structure (CGS), which provides a platform for simulating how words and their meanings evolve with respect to time. The code in this repository is basically built from scratch. The achievements I have made in this project include:  

### Model-building
1. a hydrodynamics simulation utilizing the Parcels package (http://oceanparcels.org/).

2. a Finite State Machine (FSM) mechanism implemented to determine how words of interest transform between active states and inactive states.

3. a Genetic Algorithm (GA) implemented determining how the meanings of words alter and tend to the meanings with greatest fitness.

> tutorials for how to simulate and interpret the CGSs are located in CGS_tutorials.ipynb.

### Tool-building
4. a set of ipywidgets tools, which allow easy usage of CGS using Jupyter notebook.

5. packaging of the project to allow pip installation.

6. APIs to show the simulation results in table, plot, and animation.

7. APIs to fetch word frequency data from Google n-grams database (https://books.google.com/ngrams).

> A list of APIs are located in API.md.


## Things to be done in the future  

1. future testing and development: fully test functions in the current version, develop extensions for a broader set of use cases.

2. extension to Linux and Mac platforms.

3. educational applications: development educational curricula based on the simulations.

 
