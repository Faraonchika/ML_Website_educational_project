import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import pydotplus
from sklearn.metrics import mean_squared_error
import os
import random


def r_forest(file, target, n_estimators, max_depth, min_samples_leaf, min_samples_split):
    fin_df = pd.read_excel(file, 0)
    t = list(fin_df.columns)[int(target)]

    X = fin_df.drop([t], axis=1, inplace=False)
    Y = fin_df[t]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    tree = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators, min_samples_leaf=min_samples_leaf,
                                 min_samples_split=min_samples_split)

    tree.fit(X_train, y_train)

    tree_pred = tree.predict(X_test)

    pd.DataFrame(tree_pred).to_excel("static/forest.xlsx")

    mae = mean_absolute_error(y_test, tree_pred)
    mdae = median_absolute_error(y_test, tree_pred)
    rmse = mean_squared_error(y_test, tree_pred)

    estimator = tree.estimators_[0]

    dot_data = StringIO()
    export_graphviz(estimator , out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    if os.path.exists('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/forest.png'):
        os.remove('C:/Users/Рамиль/PycharmProjects/MLSite/MainSite/static/forest.png')
    with open("static/forest.png", "wb") as png:
        png.write(graph.create_png())

    r = str(random.randint(1, 10000000))

    return mae, mdae, rmse, "static/forest.png?" + r, "/static/forest.xlsx?" + r