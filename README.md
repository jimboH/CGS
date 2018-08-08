# CGS
Contextual Geometric Structures using parcels <https://github.com/OceanParcels/parcels>

### Simulation Goals
The goals of CGS are the followings:  
1. To simulate how words and meanings change with respect to time.
2. To find out the factors that affect the meaning changing rates of words using the concept of finite state machine and genetic algorithm.

### Concepts

#### Flow field:
This project simulates with particles and environmental flow field. Each particle has a kernel, which contains a single word and a meaning of the word. Particles within the field are pushed to collide together by the flows.

#### Words:  
In CGS, a word may have many meanings, but a particle can only have one word and meaning pair. There are different mechanisms for words and meanings respectively. For words, the idea of finite state machine (FSM) is implemented to simulate the behavior of word frequency alteration. The concept is described as the image below. Words may be in 'active' or 'inactive' states. When a word is in 'active' state, it has a possibility of p to transform into 'inactive' state and a possibility of 1-p to maintain the same whenever a triggering event happens. On the other hand, when a word is in 'inactive' state, it always transform back into 'active' state after a triggering event. The triggering event in CGS is collision of particles. Something worth noticing is that the transformation possibility p should decrease with time in order to simulate the scenario that words are more likely to disappear when they are just created, but gradually turn out to be stabler afterwards.  
![](/image/word.jpg)  

#### Meanings:
In CGS, every meaning of a word is given a fitness value, which is used for genetic algorithm. Mutation occurs with given period and changes the meaning of a word to another meaning of the same word with possibility proportional to the meaning's fitness value. Therefore, if a meaning has a higher fitness value, the other meanings have higher chances to transform into this meaning.

### Installation
This project can only be installed in windows currently.  
1. Please create a virtual environment first.  
	
    $ virtualenv *environment_name* --python=2.7 --no-site-packages	  
2. Activate virtual environment.  
	  
	$ cd *path_to_environment*/Scripts  
    $ activate
3. Then install package with:
	
	$ pip install git+https://github.com/jimboH/CGS.git@master

