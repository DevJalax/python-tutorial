import numpy as np
from mlxtend.data import iris_data
X, y = iris_data()
X[:15]

def get_feature_quartiles(X):
    X_discretized = X.copy()
    for col in range(X.shape[1]):
        for q, class_label in zip([1.0, 0.75, 0.5, 0.25], [3, 2, 1, 0]):
            threshold = np.quantile(X[:, col], q=q)
            X_discretized[X[:, col] <= threshold, col] = class_label
    return X_discretized.astype(np.int)

Xd = get_feature_quartiles(X)
Xd[:15]

from sklearn.model_selection import train_test_split
Xd_train, Xd_test, y_train, y_test = train_test_split(Xd, y, random_state=0, stratify=y)

from mlxtend.classifier import OneRClassifier
oner = OneRClassifier()

oner.fit(Xd_train, y_train);

oner.feature_idx_

oner.prediction_dict_

oner.predict(Xd_train)

y_pred = oner.predict(Xd_train)
train_acc = np.mean(y_pred == y_train)  
print(f'Training accuracy {train_acc*100:.2f}%')

y_pred = oner.predict(Xd_test)
test_acc = np.mean(y_pred == y_test)  
print(f'Test accuracy {test_acc*100:.2f}%')

test_acc = oner.score(Xd_test, y_test)
print(f'Test accuracy {test_acc*100:.2f}%')
