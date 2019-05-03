import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz 


run_X = np.genfromtxt('SpringSplit_X.csv', unpack = False, delimiter = ',')
run_Y = np.genfromtxt('SpringSplit_Y.csv', unpack = False, delimiter = ',')
data_X = np.genfromtxt('newDataPoint_X.csv', unpack = False, delimiter = ',')
data_Y = np.genfromtxt('newDataPoint_Y.csv', unpack = False, delimiter = ',')
X_train , X_test , y_train , y_test = train_test_split(run_X, run_Y, stratify=run_Y, random_state=42) 


print('Training...')
tree1 = DecisionTreeClassifier( random_state = 0 )
tree2 = DecisionTreeClassifier( max_depth = 4, random_state = 0 )
tree3 = DecisionTreeClassifier( random_state = 0 )
tree1.fit (X_train, y_train ) 
tree2.fit (X_train, y_train )


print('Testing...')
print("Accuracy on training set: {:.3f}".format(tree1.score( X_train , y_train)))
print( "Accuracy on test set: {:.3f}".format(tree1.score( X_test , y_test)))
print("Accuracy on training set with pruning: {:.3f}".format(tree2.score( X_train , y_train)))
print( "Accuracy on test set with pruning: {:.3f}".format(tree2.score( X_test , y_test)))
print(tree1.predict(data_X.reshape(1,-1)))
print(data_Y)




