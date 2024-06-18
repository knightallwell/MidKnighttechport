import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import math
RGDP= pd.read_csv(r'C:/Users/timok/Downloads/RealGDP03112023.csv')
print(RGDP)
print ("#count quaterly data"+str(len(RGDP.index)))
#number of quaterly data in the data :
#analyze data
## analyze the trends of Agriculture during the years:
sns.countplot(x="Agriculture", data=RGDP)
plt.show()

