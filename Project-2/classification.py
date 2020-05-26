import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.utils import shuffle

class NaiveBayesClassifier:
    def __init__(self):
        pass

    # trans into dic
    def toDic(self, dataset):
        dic = {}

        for i in range(len(dataset)):
            item = dataset[i]

            if (item[-1] not in dic):
                dic[item[-1]] = []
            dic[item[-1]].append(item)

        return dic

    # compute mean
    def getMean(self, data):
        return sum(data) / float(len(data))

    # compute standard deviation
    def getStand(self, data):
        mean = self.getMean(data)
        stand = math.sqrt(sum([pow(x - mean, 2) for x in data]) / float(len(data) - 1))

        return stand

    # compute eigenvalues
    def getEigen(self, dataset):
        eigen = [(self.getMean(attribute), self.getStand(attribute)) for attribute in zip(*dataset)]

        del eigen[-1]
        return eigen

    # compute model
    def fit(self, X_train, y_train):
        # init
        y_train_tmp = np.array([np.array(y_train)])
        dataset = np.concatenate((X_train, y_train_tmp.T), axis=1)

        # trans into dic
        dic = self.toDic(dataset)

        # get eigenvalues
        eigenvalues = {}
        for i in dic.keys():
            eigenvalues[i] = self.getEigen(dic[i])

        self.eigenvalues = eigenvalues
        return eigenvalues

    # compute predicted values
    def getPreValues(self, x, mean, stand):
        return (1 / (math.sqrt(2 * math.pi) * stand)) * math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stand, 2))))

    # loop to process each item
    def getPre(self, item):
        pre = {}

        for i in self.eigenvalues.keys():
            pre[i] = 1
            for j in range(len(self.eigenvalues[i])):
                mean, stand = self.eigenvalues[i][j]
                pre[i] *= self.getPreValues(item[j], mean, stand)
        return pre

    # predict the value according to eigenvalues
    def predict(self, item):
        pre = self.getPre(item)

        preAttr, preValue = None, -1
        
        for i in pre.keys():
            if preAttr is None or pre[i] > preValue:
                preValue = pre[i]
                preAttr = i

        return preAttr

    # compute scores
    def getScore(self, dataset):
        score = 0
        length = len(dataset)

        for i in range(length):
            score += 1 if dataset[i][-1] == self.predictions[i] else 0

        return score / length

    # return scores
    def score(self, X_test, y_test):
        # init
        y_test_tmp = np.array([np.array(y_test)])
        dataset = np.concatenate((X_test, y_test_tmp.T), axis=1)

        # get predict values
        predictions = []
        for i in range(len(dataset)):
            predictions.append(self.predict(dataset[i]))

        self.predictions = predictions
        self.score = self.getScore(dataset)

        return self.score

# read data set and random
path = "./data/classification/train_set.csv"
dataset = pd.read_csv(path)
dataset = dataset.sample(frac=1).reset_index(drop=True)

# choose attributes
attr_group = [
    ["age", "job", "marital", "education", "balance", "housing", "loan"],
    ["contact", "duration", "campaign", "pdays", "previous", "poutcome"]
]

y = dataset['y']
fold = 10
fold_length = math.floor(y.shape[0] / fold)

# split the dataset
for idx in range(0, len(attr_group)):
    print("\n\n=====Attribute Group %d=====" % idx)
    print(attr_group[idx])
    X = dataset[attr_group[idx]]

    for i in range(0, fold):
        print("\n\n=====Round %d=====" % (i + 1))
        X_test = X.loc[i * fold_length : (i + 1) * fold_length]
        X_train = pd.concat([X.loc[0 : i * fold_length], X.loc[(i + 1) * fold_length : fold * fold_length]])

        y_test = y.loc[i * fold_length : (i + 1) * fold_length]
        y_train = pd.concat([y.loc[0 : i * fold_length], y.loc[(i + 1) * fold_length : fold * fold_length]])

        # set eigenvectors
        vec = DictVectorizer(sparse=False)
        X_train = vec.fit_transform(X_train.to_dict(orient='record'))
        X_test = vec.transform(X_test.to_dict(orient='record'))

        # random forest
        print("=====RandomForestClassifier=====")
        rfc = RandomForestClassifier()
        rfc.fit(X_train,y_train)
        print("Score: ", rfc.score(X_test, y_test))
        rfc_pre = rfc.predict(X_test)
        print(classification_report(rfc_pre, y_test))
        print("==============================")

        # gradient boosting decision tree
        print("\n=====GradientBoostingClassifier=====")
        gbc = GradientBoostingClassifier()
        gbc.fit(X_train,y_train)
        print("Score: ", gbc.score(X_test, y_test))
        gbc_pre = gbc.predict(X_test)
        print(classification_report(gbc_pre, y_test))
        print("==============================")

        # naive bayes
        print("\n=====NaiveBayesClassifier=====")
        nbc = NaiveBayesClassifier()
        nbc.fit(X_train, y_train)
        print("Score: ", nbc.score(X_test, y_test))
        print("==============================")