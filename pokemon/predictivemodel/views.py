from django.shortcuts import render
from data.models import Pokemon
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from predictivemodel.onehot import onehot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create your views here.
def predictive_index(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon
    }
    return render(request, 'predictive_index.html', context)

def create_pmodel(request):
    pokemon = Pokemon.objects.all()
    context = {
        'pokemon': pokemon,
        'result': "",
        'message': ""
    }
    df = pd.DataFrame.from_records(Pokemon.objects.all().values())
    X = []
    if request.method == "GET":
        if request.GET.get("var1", None) != "none":
            onereq = request.GET.get("var1", None)
            var1 = df[onereq]
            if not np.issubdtype(var1.dtype, np.number):
                var1 = onehot(var1)
            X.append(var1)
        if request.GET.get("var2", None) != "none":
            tworeq = request.GET.get("var2", None)
            var2 = df[tworeq]
            if not np.issubdtype(var2.dtype, np.number):
                var2 = onehot(var2)
            X.append(var2)
        if request.GET.get("var3", None) != "none":
            threereq = request.GET.get("var3", None)
            var3 = df[threereq]
            if not np.issubdtype(var3.dtype, np.number):
                var3 = onehot(var3)
            X.append(var3)
        if request.GET.get("var4", None) != "none":
            fourreq = request.GET.get("var4", None)
            var4 = df[fourreq]
            if not np.issubdtype(var4.dtype, np.number):
                var4 = onehot(var4)
            X.append(var4)
        if request.GET.get("var5", None) != "none":
            fivereq = request.GET.get("var5", None)
            var5 = df[fivereq]
            if not np.issubdtype(var5.dtype, np.number):
                var5 = onehot(var5)
            X.append(var5)
        depreq = request.GET.get("vardep", None)
        Y = df[depreq].values
    if not X:
        context = {'message': 'You must select at least 1 independent variable'}
    else:
        df = pd.concat(X, axis=1)
        x_train, x_test, y_train, y_test = train_test_split(df, Y, test_size=0.3)
        linear_model = LinearRegression(normalize=True).fit(x_train, y_train)
        y_pred = linear_model.predict(x_test)
        score = r2_score(y_test, y_pred)
        context = {'result': "Score: {}".format(score)}

    return render(request, 'predictive_index.html', context)
