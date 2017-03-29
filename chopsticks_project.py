# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:48:13 2017

@author: sujay N
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("chopstick-effectiveness.csv")
result = df.groupby("Chopstick.Length").mean().reset_index()
max_value = result["Food.Pinching.Efficiency"].max()


c = result[result["Food.Pinching.Efficiency"]== max_value]
print("Optimum chopstick length is")
print(c["Chopstick.Length"].to_string(index=False))


#Plot a Graph
plt.scatter(x=result['Chopstick.Length'], y=result['Food.Pinching.Efficiency'])      
plt.xlabel("Length of ChopSticks in mm")
plt.ylabel("Efficiency")
plt.title("Average Food Pinching Efficiency by Chopstick Length")
plt.show()
