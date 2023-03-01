import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv('TestCSV.csv')
plt.plot(data.Test3, data.Test1)
plt.show()
