# APIs  

### Module CGS_parcels.fieldset
#### Class CGS_field(x_vel, y_vel):
>CGS_field can be initialized by assigning the velocities in given positions. The velocities should be in the form of 2-dimensional numpy arrays, with positive values pointing to right or up.  
>The simulation environment of CGS is within a region of 1*1 unit square, and the velocities of flows are determined according to positions within the field.  
>For example, if the x_vel is a numpy array of [[0.5,0.2],[0.3,0.4]], then the x_directional velocity in (0.0,1,0) is 0.3.
>>Parameters:
>>>x_vel: 2-dimensional numpy array determining x_directional velocities at different positions of the field.  
>>>y_vel: 2-dimensional numpy array determining y_directional velocities at different positions of the field.

##### deploy_kernels(x_pos, y_pos, pclass):  
>Deploy kernels onto the flow field created above. The positions of kernels in x and y directions should be provided in 1-dimension numpy arrays respectively.
>>Parameters:
>>>x_pos: 1-dimensional numpy array determining initial positions of kernels in the x_dimension.  
>>>y_pos: 1-dimensional numpy array determining initial positions of kernels in the y_dimension.  
>>>pclass: Always suggested to use kernel.

##### simulate(time_length, period, output_filename, collision_thres, mutation_period):
>Do the simulation.
>>Parameters:
>>>time_length: total time length of simulation.  
>>>period: time period of simulation.  
>>>output_filename: save simulation results to the output file.  
>>>collision_thres: under what distance threshold will two kernels be considered as colliding together.  
>>>mutation_period: the period of meaning mutations.

##### word_freq_table(mode='total'):
>Show the simulation results in the form of pandas DataFrame table.   
> If the mode is selected as 'total', the total amount of kernels in both active and inactive state will be calculated and presented.  
> If the mode is selected as 'active', only the amount of kernels in active state will be presented.  
>If the mode is selected as 'all', all the information including 'total', 'active' and 'inactive' will be presented.  
>Default mode is 'total'.
>>Parameters:
>>>mode: Can be one of 'total', 'active', or 'all'.

##### plot_wordfreq(mode='total'):
>Plot the simulation results.
> If the mode is selected as 'total', the total amount of kernels in both active and inactive state will be calculated and presented.  
> If the mode is selected as 'active', only the amount of kernels in active state will be presented.  
>If the mode is selected as 'all', all the information including 'total', 'active' and 'inactive' will be presented.  
>Default mode is 'total'.
>>Parameters:
>>>mode: Can be one of 'total', 'active', or 'all'.

##### plot_trajectories(file_name,interval=200):
>Show the trajectories of the kernels within the flow field by animation.  
>Should provide filename, perhaps the same as that provided in 'simulate' function.
>>Parameters:
>>>file_name: file name of the simulation result.  
>>>interval: interval of animation. Default interval is 200.  
