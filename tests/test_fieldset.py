import pytest
import numpy as np
from CGS_parcels.fieldset import CGS_field

@pytest.mark.parametrize('x_vel',[np.array(np.reshape(np.arange(16),[4,4]),dtype=np.float32)])
@pytest.mark.parametrize('y_vel',[np.array(np.reshape(np.arange(1,17),[4,4]),dtype=np.float32)])
def test_CGS_fieldset_init(x_vel,y_vel):
    cgs = CGS_field(x_vel,y_vel)
    cg_u = cgs.fieldset.U.data
    cg_v = cgs.fieldset.V.data
    
    assert np.allclose(cg_u,np.array(np.reshape(np.arange(16),[1,4,4]),dtype=np.float32))
    assert np.allclose(cg_v,np.array(np.reshape(np.arange(1,17),[1,4,4]),dtype=np.float32))

    cg_u_grid = cgs.fieldset.U.grid
    cg_v_grid = cgs.fieldset.V.grid

    assert np.allclose(cg_u_grid.lon,np.linspace(0.0,1.0,num=4,dtype=np.float32))
    assert np.allclose(cg_v_grid.lat,np.linspace(0.0,1.0,num=4,dtype=np.float32))
