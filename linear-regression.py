import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=1/3,random_state=0) 

from sklearn.model_selection import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
y_pred = regressor.predict(X_train)

plt.scatter(X_train , Y_train , color = "blue")
plt.plot(X_train , regressor.predict(X_train) , color="red")
plt.title("train data")
plt.xlabel()
plt.ylabel()
plt.show()

plt.scatter(X_test , Y_test , color = "blue")
plt.plot(X_train , regressor.predict(X_train) , color="red")
plt.title("train data")
plt.xlabel()
plt.ylabel()
plt.show()
