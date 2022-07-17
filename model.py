# Importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

df = pd.read_csv('sample2.csv')
X = df.drop(['Segment'], axis=1)
y = df['Segment'] 
scalar = StandardScaler()
scalar = scalar.fit(X)
X = scalar.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, stratify=y, train_size=0.80, random_state=16)
KNN = KNeighborsClassifier(n_neighbors=50, weights="distance")
KNN.fit(X_train, y_train)
pickle.dump(KNN, open('model.pkl','wb'))
pickle.dump(scalar, open('scalar.pkl','wb'))
