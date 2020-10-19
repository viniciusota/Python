import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Plot scatterplot from all combinations from numeric features:
def plot_scatter( cols_list ):
for i in np.arange(0,len(num_columns)):
    if i < (len(num_columns)-1):
        sns.scatterplot( x = num_columns[i] , y = num_columns[i+1] , data = dataset)
        plt.xlabel(num_columns[i])
        plt.ylabel(num_columns[i+1])
        plt.show()


def plot_scatter_hue( cols_list , hue_list  ):
for i in np.arange(0,len(num_columns)):
    for j in cat_features:
        if i < (len(num_columns)-1):
            sns.scatterplot( x = num_columns[i] , y = num_columns[i+1] , data = dataset, hue = j)
            plt.xlabel(num_columns[i])
            plt.ylabel(num_columns[i+1])
            plt.show()
