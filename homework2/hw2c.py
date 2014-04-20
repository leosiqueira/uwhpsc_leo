# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 17:48:33 2014

@author: leosiqueira
"""

"""
Demonstration module for quadratic interpolation.

Sample solutions for Homework 2 problems #2 through #7.
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

def poly_interp(xi,yi):
    """
    General polynomial interpolation. 

    Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2,...,n-1
    where n = len(xi) = len(yi).

    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2 + ... + c[N-1]*x**(N-1).

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have the same length "
    assert len(xi)==len(yi), error_message

    # Set up linear system to interpolate through data points:
    # Uses a list comprehension, see
    # http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
    
    n = len(xi)
    c = poly.polyfit(xi, yi, n-1)

    return c

def plot_poly(xi, yi):
    """
    Perform polynomial interpolation and plot the resulting function along
    with the data points.
    """

    # Compute the coefficients:
    c = poly_interp(xi,yi)

    # Plot the resulting polynomial:
    x = np.linspace(xi.min() - 1,  xi.max() + 1, 1000)

    # Use Horner's rule:
    n = len(xi)
    y = c[n-1]
    for j in range(n-1, 0, -1):
        y = y*x + c[j-1]

    plt.figure(1)       # open plot figure window
    plt.clf()           # clear figure
    plt.plot(x,y,'b-')  # connect points with a blue line

    # Add data points  (polynomial should go through these points!)
    plt.plot(xi,yi,'ro')   # plot as red circles
    plt.ylim(yi.min()-1, yi.max()+1)       # set limits in y for plot

    plt.title("Data points and interpolating polynomial")

    plt.savefig('poly2.png')   # save figure as .png file

def test_poly1():
    """
    Test code, no return value or exception if test runs properly.
    Same points as test_cubic1.
    """
    # Generate a test by specifying c_true first:
    c_true = np.array([7., -2., -3., 1.])
    # Points to interpolate:
    xi = np.array([-1.,  0.,  1., 2.])
    # Function values to interpolate:
    # Use Horner's rule:
    n = len(xi)
    yi = c_true[n-1]
    for j in range(n-1, 0, -1):
        yi = yi*xi + c_true[j-1]

    # Now interpolate and check we get c_true back again.
    c = poly_interp(xi,yi)

    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

    # Also produce plot:
    plot_poly(xi,yi)
    

def test_poly2():
    """
    Test code, no return value or exception if test runs properly.
    Test with 5 points (quartic interpolating function).
    """
    # Generate a test by specifying c_true first:
    c_true = np.array([0., -6., 11., -6., 1.])
    # Points to interpolate:
    xi = np.array([-1.,  0.,  1., 2., 4.])
    # Function values to interpolate:
    # Use Horner's rule:
    n = len(xi)
    yi = c_true[n-1]
    for j in range(n-1, 0, -1):
        yi = yi*xi + c_true[j-1]

    # Now interpolate and check we get c_true back again.
    c = poly_interp(xi,yi)

    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

    # Also produce plot:
    plot_poly(xi,yi)
    

if __name__=="__main__":
    print "Running test..."
    test_poly1()
    test_poly2()