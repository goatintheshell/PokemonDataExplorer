from django.shortcuts import render
from data.models import Pokemon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create your views here.
def boxplot_index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'boxplot_index.html', context)

def create_boxplot(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon,
        'message': ""
    }
    df = pd.DataFrame.from_records(Pokemon.objects.all().values())
    if request.method == "GET":
        req = request.GET.get("var", None)
        data = df[req]
    if np.issubdtype(data.dtype, np.number):
        fig = plt.figure(figsize=(10, 8))
        splot = fig.add_axes([0, 0, 1, 1])
        splot.boxplot(data)
        splot.set_title("Boxplot of {}".format(data.name))
        plt.show()
    else: context = { 'message': "Variable must be numeric!"}
    return render(request, 'boxplot_index.html', context)