import pandas as pd
from matplotlib import pyplot as plt
class datademo:
    def __init__(self, file):
        self.file = file

    def show(self):
        data = pd.read_csv(self.file)
        plt.plot(data.Test1, data.Test3)
        plt.show()
