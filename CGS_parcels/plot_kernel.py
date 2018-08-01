import matplotlib
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rc
from netCDF4 import Dataset

def plot_kernel_trajectories(filename, interval=200):
    
    pfile = Dataset(filename, 'r')
    lon = np.ma.filled(pfile.variables['lon'], np.nan)
    lat = np.ma.filled(pfile.variables['lat'], np.nan)
    time = np.ma.filled(pfile.variables['time'], np.nan)
    word = np.ma.filled(pfile.variables['word'])[0,:,:]
    meaning = np.ma.filled(pfile.variables['meaning'])[0,:,:]
    color = np.ma.filled(pfile.variables['particle_color'], np.nan)
    
    time_len = lat.shape[1]
    word_shape = word.shape
    word = np.reshape(np.array([wrd.encode('ascii') for wrd in np.reshape(word,[-1])]),word_shape)
    meaning = np.reshape(np.array([mng.encode('ascii') for mng in np.reshape(meaning,[-1])]),word_shape)
    pairs = [(word[i,j]+':'+meaning[i,j]) for i in range(word_shape[0]) for j in range(word_shape[1])]
    legends = list(set(pairs))
    wrd_mng = np.reshape(np.array(pairs),word_shape)
        
    fig = plt.figure()
    ax = plt.axes(xlim=(np.nanmin(lon), np.nanmax(lon)), ylim=(np.nanmin(lat), np.nanmax(lat)))
    plottimes = np.unique(time)
    plottimes = plottimes[~np.isnan(plottimes)]
    b = time == plottimes[0]
    scat = ax.scatter(lon[b], lat[b], s=60, c=color[b])
    ttl = ax.set_title('Particle at time ' + str(plottimes[0]))
    frames = np.arange(1, len(plottimes))

    def animate(t):
        ax.cla()
        ax.set_xlim(np.nanmin(lon), np.nanmax(lon))
        ax.set_ylim(np.nanmin(lat), np.nanmax(lat))

        for j in range(len(legends)):
            try:
                idx = wrd_mng[:,t]==legends[j]
                lat_ = np.reshape(np.array(lat[idx],dtype=np.float32),[-1,time_len])
                lon_ = np.reshape(np.array(lon[idx],dtype=np.float32),[-1,time_len])
                color_ = np.reshape(np.array(color[idx],dtype=np.float32),[-1,time_len])
                time_ = np.reshape(np.array(time[idx],dtype=np.float32),[-1,time_len])
                b = time_ == plottimes[t]
                clr = color_[b][0]
                clr = [1-clr,clr/2,clr]
            except:
                continue
            ax.scatter(lon_[b], lat_[b], s=60, c=clr, label=legends[j])
            ax.legend(loc=1)
        ttl.set_text('Particle at time ' + str(plottimes[t]))
        return scat,

    rc('animation', html='jshtml')
    anim = animation.FuncAnimation(fig, animate, frames=frames,
                                   interval=interval, blit=False)


    plt.close()
    return anim
