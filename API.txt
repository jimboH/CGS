# APIs  

Module | class | functions  
----|----|----  
CGS_parcels.fieldset|CGS_field(x_vel, y_vel)|1.deploy_kernels(x_pos,y_pos,pclass)<br> 2.

CGS_field can be initialized by assigning the velocities in given positions. The velocities should be in the form of 2-dimensional numpy arrays, with postive values pointing to right or up.
        The simulation environment of CGS is within a region of 1*1 unit square, and the velocities of flows are detemined
        according to positions within the field. For example, if the x_vel is a numpy array of [[0.5,0.2],[0.3,0.4]], then
        the x_directional velocity in (0.0,1,0) is 0.3.
        """
