# %%
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import csv

df=pd.read_csv(r'C:\Users\mihir\Downloads\disaster-events new.csv')
print(df.head())
print(df.columns)
print(df.get('Earthquake'))



# %%
#print(df.Disasters)
print(df.Entity)



