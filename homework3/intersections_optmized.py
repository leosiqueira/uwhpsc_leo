# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:48:56 2014

@author: leosiqueira
"""
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def findIntersection(f, g, x0):
    return fsolve(lambda x : f(x) - g(x), x0, xtol = 1e-12, full_output = True)

def test1():
    """
    Test findintersection of two functions using different initial
    conditions.
    """
    g1vals = lambda x : x*np.cos(np.pi*x)
    g2vals = lambda x :  1.- 0.6*x**2
    x = np.linspace(-10,10,1000)
    plt.figure(1)
    plt.clf()
    plt.plot(x, g1vals(x), 'b', x, g2vals(x), 'r')
    plt.legend(['g1','g2'])
    
    for x0 in [-2.2, -1.6, -0.8, 1.45]:
        res = findIntersection(g1vals, g2vals,x0)
        print "%s" % res[3]
        print "solve returns x = %22.15e after %s calls " % (res[0][0], res[1]['nfev'])
        fx = g1vals(res[0][0]) - g2vals(res[0][0])
        print "    f(x) = %22.15e" % fx
        plt.plot(res[0][0],g1vals(res[0][0]),'ko')
        
    plt.axis([-5, 5, -4, 4]) 
    plt.grid()   
    plt.show()

