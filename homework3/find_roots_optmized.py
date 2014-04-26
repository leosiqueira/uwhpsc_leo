# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:11:59 2014

@author: leosiqueira
"""
from scipy.optimize import fsolve

fval_sqrt = lambda x : x**2 - 4

def test1():
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        print 'Initial guess: x = %22.15e' % x0
        x = fsolve(fval_sqrt, x0, xtol = 1e-14, full_output = True )
        print "%s" % x[3]
        print "solve returns x = %22.15e after %s calls " % (x[0][0], x[1]['nfev'])
        f = fval_sqrt(x[0][0])
        print "the value of f(x) is %22.15e" % f
        assert abs(x[0][0]-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x[0][0]
