import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
from django import template
from data.models import Pokemon

df = pd.DataFrame.from_records(Pokemon.objects.all().values())

var1 = df.height_m
var2 = df.weight_kg
h = 6
w = 10

def create_scatterplot(x, y, h, w):
    if np.issubdtype(x.dtype, np.number) and np.issubdtype(y.dtype, np.number):
        X, Y = x.values, y.values
        X, Y = X.reshape(-1, 1), Y.reshape(-1, 1)
        fig = plt.figure(figsize=(w, h))
        splot = fig.add_axes([0, 0, 1, 1])
        splot.scatter(x, y)
        splot.set_xlabel(x.name)
        splot.set_ylabel(y.name)
        splot.set_title("Scatterplot of {} vs {}".format(x.name, y.name))
        plt.plot(X, LinearRegression().fit(X, Y).predict(X), color="r")
        plt.show()
    else:
        print("Variables must be numeric")


create_scatterplot(var1, var2, h, w)
