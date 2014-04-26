# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 10:08:35 2014

@author: leosiqueira
"""

def solve(fvals, x0, debug = False):
    """ Estimate the zero of f(x) using Newton's method. 
     *Input*
      fvals:  tuple containing the function to find a root of
              and its derivative (f, f').
      x0: the initial guess
      debug: logical, prints iterations if debug= True.
     **Returns**
       the estimate x satisfying f(x)=0 (assumes Newton converged!) 
       the number of iterations iter."""
    # initial guess
    x = x0
    if debug:
        print 'Initial guess: x = %22.15e' % x0
    # Newton iteration to find a zero of f(x) 
    maxiter = 20
    tol = 1e-14
    for k in range(maxiter):
        # evaluate function and its derivative:
        f, fp = fvals(x)
        if (abs(f) < tol):
            break
        # compute Newton increment x:
        deltax = f / fp
        # update x:
        x = x - deltax
        if debug:
            print 'After %s iterations, x = %22.15e' % (k+1,x)
    if (k == maxiter-1):
        # might not have converged
        f, fp = fvals(x)
        if (abs(f) > tol):
            print '*** Warning: has not yet converged'
            return x, k+1
    else:
        return x, k

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        print 'Initial guess: x = %22.15e' % x0
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
    
       
    