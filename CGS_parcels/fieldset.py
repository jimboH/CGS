import parcels
import sys
import numpy as np
from datetime import timedelta
from argparse import ArgumentParser
from CGS_parcels.plot_kernel import plot_kernel_trajectories
from CGS_parcels.kernel import kernel_set
from CGS_parcels.kernel_file import kernel_file
from CGS_parcels.advection import self_AdvectionRK4

class CGS_field:
    """CGS flow field that simulates the environmental flows.
    The field can be initialized by the velocities of flows in given positions.
    """
    
    def __init__(self,x_vel,y_vel):
        """CGS field can be initialized by assigning the velocities in given positions.
        The velocities should be in the form of 2-dimensional numpy arrays, with postive values pointing to right or up.
        For example, if x_vel is [[1,1,1,1],[5,5,5,5]], it means that the velocities in x direction are 1 when y is 1, and 
        are 5 when y is 2. If the velocities are negative, it means the velocities go in negative x direction(to the left).
        """
        
        ## make sure the dimensions of x_vel are equal to those of y_vel
        if x_vel.shape != y_vel.shape:
            raise RuntimeError("The dimensions of x_vel should be the same as those of y_vel")
        
        self.x_velocities = x_vel
        self.y_velocities = y_vel
        
        ## initialize parcels fields with lon and lat values set according to the len(x_vel) and len(y_vel)
        field_x = parcels.Field(name='U',data=x_vel,lon=np.linspace(start=0,stop=1,num=len(x_vel[0])),\
                                lat=np.linspace(start=0,stop=1,num=len(x_vel)))
        field_y = parcels.Field(name='V',data=y_vel,lon=np.linspace(start=0,stop=1,num=len(y_vel[0])),\
                                lat=np.linspace(start=0,stop=1,num=len(y_vel)))
        
        ## initialize parcels fieldsets with fields created above
        fieldset = parcels.FieldSet(U=field_x,V=field_y)
        
        self.fieldset = fieldset
        
    def deploy_kernels(self,x_pos,y_pos,pclass):
        """Deploy kernels on the flow field created above. 
        The postions of kernels in x and y directions should be provided in 1-dimension numpy arrays respectively.
        For example, if two kernels are created, and the x_pos and y_pos are set as [1,2] and [3,4], then
        the positions of the kernels will be at [1,3] and [2,4] respectively.
        """
        
        ## set the pclass to be self-defined kernel
        
        ## the kernels should be customized in the future
        kset = kernel_set(fieldset=self.fieldset,pclass=pclass,lon=x_pos,lat=y_pos)
        self.kset = kset
    
    def simulate(self,time_length,period,output_filename,collision_thres,mutation_period):
        """Do the simulation.
        The total time length and period of simulation should be provided.
        """
        ## do the simulation with time information provided above. outputfile updated with period provided above.
        kset = self.kset
        data = kset.execute(collision_thres,mutation_period,pyfunc=self_AdvectionRK4,runtime=timedelta(minutes=time_length),\
                            dt=timedelta(minutes=period),output_file=kernel_file(name=output_filename,\
                                                     particleset=kset,outputdt=timedelta(minutes=period)))
        self.kernel_FSM = data

    def word_freq_table(self):
        return self.kernel_FSM
       
    def plot_wordfreq(self):
        data = self.kernel_FSM
        data.plot(x='time',y=data.columns.values[1:])
        
    def plot_trajectories(self,file_name,interval=200):
        """Plot the trajectories of the kernels within the flow field.
        Can choose the moving mode to show the animated trajectories.
        """
        return plot_kernel_trajectories(file_name+'.nc', interval)

def main(argv):
    print('main')

if __name__ == "__main__":
    main(sys.argv)
