# APIs  

Module | class | functions  
----|----|----  
CGS_parcels.fieldset|CGS_field(x_vel, y_vel)|1. deploy_kernels(x_pos,y_pos,pclass)<br> 2. simulate(time_length, period, output_filename, collision_thres, mutation_period)<br>3. word_freq_table(mode='total')<br>4. plot_wordfreq(mode='total')<br>5. plot_trajectories(file_name,interval=200)  

Module | class | functions  
----|----|----
CGS_parcels.kernel|kernel_set(fieldset, pclass=kernel, lon=[], lat=[], depth=None, time=None, repeatdt=None)|set_kernel(word_meaning_freq_fit,prob=0.5,ratio=0.5)

Module | class | functions  
----|----|----
CGS_parcels.plot_kernel||plot_kernel_trajectories(filename, interval=200)

Module | class | functions  
----|----|----
CGS_parcels.ngrams||1. getNgrams(query, startYear, endYear,smoothing=0,case_insensitive=False)<br>2. use_ngram(word_meaning,year)

Module | class | functions  
----|----|----
CGS_parcels.CGS_notebook_tool|CGS_field_initializer(**kwargs)|1. display()<br>2. build(word_meaning_freq_fit=None,collision_thres=1e-4,mutation_period=5,field_set=None,particle_set=None)<br>3. plot()<br>4. animate(interval=200)<br>5. table()
