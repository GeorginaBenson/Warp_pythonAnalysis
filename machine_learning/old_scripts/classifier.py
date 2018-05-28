#!/usr/bin/env python3

#print(__doc__)


# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn import datasets

h = .02  # step size in the mesh

names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    #KNeighborsClassifier(n_neighbors=3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

iris = datasets.load_iris()
#X = iris.data[:, 0:2]  # we only take the first two features for visualization
#y = iris.target
X, y = make_classification(n_features=4, n_redundant=0, n_informative=4,
                          random_state=1, n_clusters_per_class=1)
rng = np.random.RandomState(4)
#X += 3 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [iris.data, iris.target]
#datasets = [make_moons(noise=0.3, random_state=0),
#            make_circles(noise=0.2, factor=0.5, random_state=1),
#           linearly_separable]
           
X, y = iris.data[:, 0:4] , iris.target
print(datasets)
#print(min(X[:, 0]))
#print(min(X[:, 1]))
#print(min(X[:, 2]))
#print(min(X[:, 3]))

figure = plt.figure(figsize=(27, 9))
i = 1
# iterate over datasets
for ds_cnt, ds in enumerate(datasets):
    # preprocess dataset, split into training and test part
    #print(ds)
    #print(ds_cnt)
    X, y = iris.data[:, 0:4] , iris.target
    print(X)
    print(y.shape)
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    #x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    #y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    #xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    #                     np.arange(y_min, y_max, h))
#    print(xx.shape)

    xx = np.linspace(3, 9, 100)
    yy = np.linspace(1, 5, 100).T
    zz = np.linspace(0, 8, 100)
    aa = np.linspace(0, 3, 100).T
    xx, yy, zz, aa = np.meshgrid(xx, yy, zz, aa)

    # just plot the dataset first
    cm = plt.cm.RdBu
    cm_bright = ListedColormap(['#FF0000', '#0000FF'])
    ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
    if ds_cnt == 0:
        ax.set_title("Input data")
    # Plot the training points
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
               edgecolors='k')
    # and testing points
    ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6,
               edgecolors='k')
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    i += 1

    # iterate over classifiers
    for name, clf in zip(names, classifiers):
        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)
        print(np.c_[X])

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, x_max]x[y_min, y_max].
        if hasattr(clf, "decision_function"):
            Z = clf.decision_function(np.r_['1,4,0', xx.ravel(), yy.ravel(), zz.ravel(), aa.ravel()])
        else:
            Z = clf.predict_proba(np.r_['1,4,0', xx.ravel(), yy.ravel(), zz.ravel(), aa.ravel()])

        # Put the result into a color plot
        #print(Z)
        #print("z size = {}".format(Z.size))
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

        # Plot also the training points
        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                   edgecolors='k')
        # and testing points
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
                   edgecolors='k', alpha=0.6)

        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        if ds_cnt == 0:
            ax.set_title(name)
        ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                size=15, horizontalalignment='right')
        i += 1

plt.tight_layout()
plt.show()
