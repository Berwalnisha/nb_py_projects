# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:30:45 2022

@author: lenovo
"""

import numpy as np

#gradient descent function
def gradient_descent(x,y,theta_1,theta_0):
    iteration=1000
    n=len(x)
    learningrate=0.05
    for i in range(iteration):
        y_predicted=theta_1*x*theta_0
        #calculate cost function
        cost=(1/n)*sum([val**2 for val in (y_predicted-y)])
        #partial derivative with respect to theha_1
        md=(1/n)*sum(x*(y_predicted-y))
        #partial derivative with respect to theta_0
        bd=(1/n)*sum(y_predicted-y)
        theta_1=theta_0 - learningrate*md
        theta_0=theta_0 - learningrate*bd
        #print all values
        print("m {},b{},iteration{}". format(theta_1,theta_0,i))
    return theta_0,theta_1  
    
x=np.array([1,2,3,4,5,6])
y=np.array([5,7,9,11,12,19]) 
theta_1=theta_0=0
theta_0,theta_1=gradient_descent(x,y,theta_1,theta_0)
#print("theta_1 {},theta_0 {}". format(theta_1.theta_0))
val = input("enter your house size:")
y=theta_0+theta_1*np.float64(val)
print(y)
    
    
    