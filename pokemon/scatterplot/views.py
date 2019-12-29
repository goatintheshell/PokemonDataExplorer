from django.shortcuts import render
from data.models import Pokemon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create your views here.
def scatterplot_index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'scatterplot_index.html', context)

def create_scatterplot(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon,
        'message': ""
    }
    df = pd.DataFrame.from_records(Pokemon.objects.all().values())
    if request.method == "GET":
        xreq = request.GET.get("varX", None)
        x = df[xreq]
        yreq = request.GET.get("varY", None)
        y = df[yreq]
    if np.issubdtype(x.dtype, np.number) and np.issubdtype(y.dtype, np.number):
        X, Y = x.values, y.values
        X, Y = X.reshape(-1, 1), Y.reshape(-1, 1)
        fig = plt.figure(figsize=(10, 8))
        splot = fig.add_axes([0, 0, 1, 1])
        splot.scatter(x, y)
        splot.set_xlabel(x.name)
        splot.set_ylabel(y.name)
        splot.set_title("Scatterplot of {} vs {}".format(x.name, y.name))
        plt.plot(X, LinearRegression().fit(X, Y).predict(X), color="r")
        plt.show()
    else: context = { 'message': "Variables must be numeric!"}
    return render(request, 'scatterplot_index.html', context)
