from sklearn import preprocessing
import pandas as pd

def onehot(var):
    encoded = preprocessing.OneHotEncoder(sparse=False).fit(var.values.reshape(-1, 1))
    labels = encoded.transform(var.values.reshape(-1, 1))
    print(labels)
    encoded_var = pd.DataFrame()
    for x in range(len(encoded.categories_)):
        encoded_var["{}".format(encoded.categories_[x])] = labels[:, x]
    return encoded_var
