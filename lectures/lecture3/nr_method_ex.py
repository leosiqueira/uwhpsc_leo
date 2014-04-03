# -*- coding: utf-8 -*-
"""
Find root using Newton-Raphson method in sympy

Created on Thu Apr  3 14:46:36 2014

@author: leo.siqueira
"""

from nr_sympy import NR_method

fx = '4-x**2'
print "\n Compute root of %s using newtons method...\n" %(fx)
s= 1.0
r = NR_method(fx, s)
fx = '9-x**2'
print "\n Compute root of %s using newtons method...\n" %(fx)
r2 = NR_method(fx, s, p=5.e-6)