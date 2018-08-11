import pytest
import numpy as np
from CGS_parcels.fieldset import CGS_field

@pytest.mark.parametrize('x_vel',[1,2,3,4])
@pytest.mark.parametrize('y_vel',[2,3,4,5])
def test_CGS_fieldset_init(x_vel,y_vel):
    cgs = CGS_field(x_vel,y_vel)
    
