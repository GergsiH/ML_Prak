import numpy as np


class Preprocessor:

    def __init__(self):
        pass

    def fit(self, X, Y=None):
        pass

    def transform(self, X):
        pass

    def fit_transform(self, X, Y=None):
        pass


class MyOneHotEncoder(Preprocessor):

    def __init__(self, dtype=np.float64):
        super().__init__()
        self.dtype = dtype

    def fit(self, X, Y=None):
        """
        param X: training objects, pandas DataFrame, shape [n_objects, n_features]
        param Y: unused
        """
        self.unique = []
        x = X.to_numpy()

        for j in range(x.shape[1]):
            temp = []
            for i in range(x.shape[0]):
                if x[i][j] not in temp:
                    temp.append(x[i][j])
            self.unique.append(sorted(temp))

    def transform(self, X):
        """
        param X: objects to transform, pandas DataFrame, shape [n_objects, n_features]
        returns: transformed objects, numpy array, shape [n_objects, |f1| + |f2| + ...]
        """
        x = X.to_numpy()
        answer = None

        for j in range(x.shape[1]):
            temp = np.zeros((x.shape[0], len(self.unique[j])))
            for i in range(x.shape[0]):
                for index, elem in enumerate(self.unique[j]):
                    if elem == x[i][j]:
                        temp[i][index] = 1
                        break

            answer = temp if answer is None else np.concatenate((answer, temp), axis=1)

        return answer

    def fit_transform(self, X, Y=None):
        self.fit(X)
        return self.transform(X)

    def get_params(self, deep=True):
        return {"dtype": self.dtype}


class SimpleCounterEncoder:

    def __init__(self, dtype=np.float64):
        self.dtype = dtype

    def fit(self, X, Y):
        """
        param X: training objects, pandas DataFrame, shape [n_objects, n_features]
        param Y: target for training objects, pandas Series, shape [n_objects,]
        """
        x = X.to_numpy()
        y = Y.to_numpy()
        self.dictinory = []

        for j in range(x.shape[1]):
            temp = {}
            for i in range(x.shape[0]):
                if x[i][j] not in temp:
                    counters = 0
                    successes = 0

                    for i1 in range(x.shape[0]):
                        if x[i1][j] == x[i][j]:
                            counters += 1
                            successes += y[i1]

                    successes = successes / counters
                    counters = counters / x.shape[0]
                    temp[x[i][j]] = np.array([successes, counters, 0])

            self.dictinory.append(temp)

    def transform(self, X, a=1e-5, b=1e-5):
        """
        param X: objects to transform, pandas DataFrame, shape [n_objects, n_features]
        param a: constant for counters, float
        param b: constant for counters, float
        returns: transformed objects, numpy array, shape [n_objects, 3 * n_features]
        """
        x = X.to_numpy()
        answer = None

        for j in range(x.shape[1]):
            temp = np.zeros((x.shape[0], 3))

            for i in range(x.shape[0]):
                temp[i] = self.dictinory[j][x[i][j]]
                temp[i][2] = (temp[i][0] + a) / (temp[i][1] + b)

            answer = temp if answer is None else np.concatenate((answer, temp), axis=1)

        return answer

    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)

    def get_params(self, deep=True):
        return {"dtype": self.dtype}


def group_k_fold(size, n_splits=3, seed=1):
    idx = np.arange(size)
    np.random.seed(seed)
    idx = np.random.permutation(idx)
    n = size // n_splits

    for i in range(n_splits - 1):
        yield idx[i * n: (i + 1) * n], np.hstack((idx[:i * n], idx[(i + 1) * n:]))

    yield idx[(n_splits - 1) * n:], idx[:(n_splits - 1) * n]


class FoldCounters:

    def __init__(self, n_folds=3, dtype=np.float64):
        self.dtype = dtype
        self.n_folds = n_folds

    def fit(self, X, Y, seed=1):
        """
        param X: training objects, pandas DataFrame, shape [n_objects, n_features]
        param Y: target for training objects, pandas Series, shape [n_objects,]
        param seed: random seed, int
        """
        self.groups = group_k_fold(X.shape[0], self.n_folds, seed)
        self.answer = []

        for val, train in self.groups:
            sce = SimpleCounterEncoder()
            sce.fit(X.iloc[train], Y.iloc[train])
            self.answer.append((val, sce))

    def transform(self, X, a=1e-5, b=1e-5):
        """
        param X: objects to transform, pandas DataFrame, shape [n_objects, n_features]
        param a: constant for counters, float
        param b: constant for counters, float
        returns: transformed objects, numpy array, shape [n_objects, 3 * n_features]
        """
        temp = None

        for val, class1 in self.answer:
            con = np.concatenate((class1.transform(X.iloc[val], a, b), np.reshape(np.array(val), (len(val), 1))), axis=1)

            temp = con if temp is None else np.concatenate((temp, con), axis=0)

        temp = temp[temp[:, -1].argsort()]

        return np.delete(temp, -1, axis=1)

    def fit_transform(self, X, Y, a=1e-5, b=1e-5):
        self.fit(X, Y)
        return self.transform(X, a, b)


def weights(x, y):
    """
    param x: training set of one feature, numpy array, shape [n_objects,]
    param y: target for training objects, numpy array, shape [n_objects,]
    returns: optimal weights, numpy array, shape [|x unique values|,]
    """
    set_temp = set(x)
    w = np.array([0.0] * len(set_temp))

    for i, elem in enumerate(set_temp):
        w[i] = sum(y[x == elem]) / list(x).count(elem)

    return w
