# -*- coding: utf-8 -*-
"""
Example that returns all of the iteration numbers of Netwons method for a given function into pretty colors.

Created on Thu Apr  3 15:27:25 2014

@author: leo.siqueira
"""
#import numpy as np
import matplotlib.pyplot as plt
from np_julia_set import plot_fractal

# Make a function to iterate over.
# The lambda keyword in Python is great for making short one-line functions
print '\n Creating Newtons Method (x^3-1) fractal...'
j_fn = lambda x: x**3-1    
opt1 = {'title':'Newtons Method ($x^3-1$)'}
plot_fractal(j_fn, 600, 600, opt1)
plt.savefig('newton_julia_set.png')

print '\n Creating Newtons Method (x^4-1) fractal...'
# second case f(x) = x^4-1
j_fn = lambda x: x**4-1  
opt2 = {'title':'Newtons Method ($x^4-1$)'}
plot_fractal(j_fn, 600, 600, opt2)
plt.savefig('newton_julia_set2.png')
plt.show()