# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'./disaster-events new.csv')


df_filtered = df[(df['Year'] >= 2018) & (df['Disasters'])]

plt.plot(df_filtered['Year'], df_filtered['Disasters'], marker='o', linestyle='-')

plt.title('Number of Disasters Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Disasters')


plt.grid(True)


plt.show()


    

  


