#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:27:13 2020

@author: max
"""


import numpy as np
import matplotlib.pyplot as plt

print('Exercise 2.10')

a_1 = 15.8
a_2 = 18.3
a_3 = .714
a_4 = 23.2

def B(A,Z, a_5):
    return a_1*A - a_2*A**(2/3) - a_3*(Z**2/A**(1/3)) -    (
    a_4*((A-2*Z)**2/A) + a_5 / A**(1/2)             )
    
A = 58
Z = 28
a_5 = 12
print('Part a) {} MeV'.format(round(B(A, Z, a_5), 1)))

print('Part b) {} MeV'.format(round(B(A, Z, a_5)/A, 1)))

B = a_1*A - a_2*A**(2/3) - a_3*(Z**2/A**(1/3)) -    (
    a_4*((A-2*Z)**2/A) + a_5 / A**(1/2)             )
 
def B(Z):
    A = range(Z, 3*Z+1)
    a_5 = []
    B_values = []
    for i in range(0,len(A)):
        if A[i] % 2 != 0:
            a_5.append(0)
        if A[i] % 2 == 0 and Z % 2 == 0:
            a_5.append(12)
        elif A[i] % 2 == 0 and Z % 2 != 0:
            a_5.append(-12)
            
    for i in range(0,len(A)):
        B_values.append(a_1*A[i] - a_2*A[i]**(2/3) - a_3*(Z**2/A[i]**(1/3)) -(
            a_4*((A[i]-2*Z)**2/A[i]) + a_5[i] / A[i]**(1/2))                 )
    
    for i in range(0,len(B_values)):
        if B_values[i] == max(B_values):
            element_number = i

    print('Part c)\n\tThe maximum value for B occurs when A = {}\n'
          '\tThe binding energy per nucleon is: {} MeV'.format(
              A[element_number], B_values[element_number]/A[element_number]))

B(28)

print('Part d)\n')
B_over_As = []
Z = np.arange(1,101)
for z in range(0,len(Z)):
    
    L = Z[z]
    A = range(L, 3*L+1)
    a_5 = []
    B_values = []
    
    for i in range(0,len(A)):
        if A[i] % 2 != 0:
            a_5.append(0)
        if A[i] % 2 == 0 and L % 2 == 0:
            a_5.append(12)
        elif A[i] % 2 == 0 and L % 2 != 0:
            a_5.append(-12)
            
    for i in range(0,len(A)):
        B_values.append(a_1*A[i] - a_2*A[i]**(2/3) - a_3*(L**2/A[i]**(1/3)) -(
            a_4*((A[i]-2*L)**2/A[i]) + a_5[i] / A[i]**(1/2))                 )
    
    for i in range(0,len(B_values)):
        if B_values[i] == max(B_values):
            element_number = i
            
    B_over_As.append(B_values[element_number]/A[element_number])
    
    print('\tThe most stable value of A when Z = {} is {}\n'
          .format(L,A[element_number]))

for i in range(0,len(B_over_As)):
    if B_over_As[i] == max(B_over_As):
        Best_Z = Z[i]

print('\tThe maximum binding energy per nucleon occurs when Z is: {}'.format(Best_Z))