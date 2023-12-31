import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
import sys




def visualize(dataframe):
    plot = dataframe.plot().get_figure()
    #plot.save_fig("plot1.pdf")
    plt.savefig('plot1.pdf')
    

