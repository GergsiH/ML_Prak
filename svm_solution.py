import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline


def train_svm_and_predict(train_features, train_target, test_features):
    """
    train_features: np.array, (num_elements_train x num_features) - train data description, the same features and the same order as in train data
    train_target: np.array, (num_elements_train) - train data target
    test_features: np.array, (num_elements_test x num_features) -- some test data, features are in the same order as train features

    return: np.array, (num_elements_test) - test data predicted target, 1d array
    """
    pipeline = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=2, gamma="auto", class_weight="balanced"))

    pipeline.fit(train_features, train_target)

    pred = pipeline.predict(test_features)
    return pred
