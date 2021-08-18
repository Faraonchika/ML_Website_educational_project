from flask import render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.metrics import mean_squared_error
import os
import random


def tree_learn(file, target, max_depth, min_samples_split, min_samples_leaf, max_features):
    fin_df = pd.read_excel(file, 0)
    t = list(fin_df.columns)[int(target)]

    X = fin_df.drop([t], axis=1, inplace=False)
    Y = fin_df[t]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    tree = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split,
                                  min_samples_leaf=min_samples_leaf,  max_features=max_features)

    tree.fit(X_train, y_train)

    tree_pred = tree.predict(X_test)

    pd.DataFrame(tree_pred).to_excel("static/tree.xlsx")

    mae = mean_absolute_error(y_test, tree_pred)
    mdae = median_absolute_error(y_test, tree_pred)
    rmse = mean_squared_error(y_test, tree_pred)

    dot_data = StringIO()
    export_graphviz(tree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    if os.path.exists('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/1.png'):
        os.remove('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/1.png')
    with open("static/1.png", "wb") as png:
        png.write(graph.create_png())

    r = str(random.randint(1, 10000000))

    return mae, mdae, rmse, "static/1.png?" + r, "/static/tree.xlsx?" + r
