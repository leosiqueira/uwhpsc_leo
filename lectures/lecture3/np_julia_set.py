# -*- coding: utf-8 -*-
"""
Return all of the iteration numbers of Netwons method for a given function into pretty colors.

Created on Thu Apr  3 16:40:10 2014

@author: leo.siqueira
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def julia_color(fn, z0, max_iter = None, eps = 1.e-14 ,escape = 10000.0):
    """ Newton-Raphson “solver” for function fn will receive the precision (optional)
    with default value of 1.e-14 and z0 the starting guess value.
    **Arguments:**
    *fn*
        input function.
    *z0* 
       initial guess .
    **Optional arguments:**
    *eps*
       precision.
    *escape*
       z escaping.
     
    **Returns:**
    *idx_iter*
    iteration index.
        
    **Example:**  
    ex: colors[idx_x, idx_y] = julia_color(fn, complex(xs[idx_x], ys[idx_y]))
    
    """
    # Initial guess
    z = z0
    if max_iter is None: max_iter = 50 # max iterations allowed
    ds = 1.e-3 #1e - 6 # step size for numerical derivative
    if eps is None: eps = 1.e-14 #1e - 14 # max error allowed
    for idx_iter in xrange(max_iter):
        # Apply Newtons method.
        dz = (fn (z + complex (ds, ds)) - fn (z))/complex (ds, ds)
        z0 = z - fn (z)/dz # Newton iteration
        if abs (z0 - z) < eps : # stop when close enough to any root
            break
        z = z0      
        # Has z escaped yet? If so, return how long it took.
        if np.abs(z) > escape:
            return idx_iter
        
    # If we ran out of iterations, just return the maximum number
    # of iterations we were willing to run.
    return idx_iter

def plot_fractal(fn, n_x, n_y, plotOpt=None, x_min=-1, x_max=1, y_min=-1, y_max=1):
    """ Newton-Raphson iteration plotter for function fn, with number of points x and y image matrix.
    **Arguments:**
    *fn*
        input function to be passed to julia_color().
    *nx* 
       number of points in x.
    *ny* 
       number of points in y. 
    **Optional arguments:**
    *plotOpt*
     dictionary with plotting options.
     
    **Returns:**
     Figure
        
    **Example:**  
    ex: j_fn = lambda x: x**3-1    
    opt1 = {'title':'Newtons Method (x^3-1)'}
    plot_fractal(j_fn, 600, 600, opt1) """   
    
    if plotOpt is None: plotOpt = {} # initialize plotopt dic
    colors = np.empty((n_x, n_y)) # initialize colors matrix
    xs = np.linspace(x_min, x_max, n_x)
    ys = np.linspace(y_min, y_max, n_y)
    start_time = time.time() # time counter
    for idx_x in xrange(n_x):
        for idx_y in xrange(n_y):
            colors[idx_x, idx_y] = julia_color(fn, complex(xs[idx_x], ys[idx_y]))
            
    total_time = time.time() - start_time
    plt.figure(figsize=(n_x / 80, n_y / 80))
    plt.imshow(colors, extent=(x_min, x_max, y_min, y_max))
    title = plotOpt.get('title', 'Newtons method Julia set fractal')
    plt.title(title) 
    print 'Finished in %10.6f seconds'%(total_time,)