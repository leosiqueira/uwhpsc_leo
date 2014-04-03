# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 13:28:57 2014

Newton-Raphson “solver” will receive the precision (optional)
with default value of p = 1.e-14, the function representation
in a SymPy compatible format and letting x be the symbolic variable 
and s the starting guess value.
"""

import sys, time
from sympy import *

"""
Newton-Raphson “solver” will receive the precision (optional)
with default value of 5⋅10-6, the function representation
in a SymPy compatible format and letting x be the symbolic variable 
and the starting guess value.

"""

def NR_method(fx, s, p = None): 
    """
    Newton-Raphson “solver” will receive the precision (optional)
    with default value of 1.e-14, the function representation
    in a SymPy compatible format and letting x be the symbolic variable 
    and s the starting guess value.
    **Arguments:**
    *fx*
        input sym function.
    *s* 
       initial guess .
    **Optional arguments:**
    *p*
       precision.
     
    **Returns:**
    *r*
    root of fx.
        
    **Example:**  
    ex: fx = '4-x**2'
        s = 910
        r1 = NR_method(f,s) 
        p = 1.e-14
        r2 = NR_method(f,s,p)
    
    """
    start_time = time.time()
    if p is None: p = 1.e-14
    sym_x = Symbol('x')
    # convert the given function to a symbolic expression
    try:
      fx = S(fx)
    except:
      sys.exit('Unable to convert function to symbolic expression.')
     
    # calculate the differential of the function
    try:
      dfdx = diff(fx, Symbol('x'))
    except:
      sys.exit('Unable to differentiate function.')
     
    # e is the relative error between 2 consecutive estimations of the root
    e = 1
    x0 = s
    iterations = 0
     
    while ( e > p ):
      # new root estimation
      try:   
        r = x0 - fx.subs({sym_x : x0})/dfdx.subs({sym_x : x0})
      except ZeroDivisionError:
        print "Function derivative is zero. Division by zero, program will terminate."
        sys.exit()
      # relative error
      e = abs((r - x0)/r)
      iterations += 1
      x0 = r
     
    total_time = time.time() - start_time
     
    print 'Function:'
    pprint(fx)
    print 'Derivative:'
    pprint(dfdx)
    print 'Root %10.6f calculated after %d iterations'%(r, iterations)
    print 'Root %10.6f calculated with %e precision'%(r, p)
    print 'Function value at root %10.6f'%(fx.subs({sym_x : r}),)
    print 'Finished in %10.6f seconds'%(total_time,)
    return r