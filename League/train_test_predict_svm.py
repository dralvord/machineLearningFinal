import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
 
data_X = np.genfromtxt('newDataPoint_X.csv', unpack = False, delimiter = ',')
data_Y = np.genfromtxt('newDataPoint_Y.csv', unpack = False, delimiter = ',')
run_X = np.genfromtxt('SpringSplit_X.csv', unpack = False, delimiter = ',')
run_Y = np.genfromtxt('SpringSplit_Y.csv', unpack = False, delimiter = ',') 
X_train , X_test , y_train , y_test = train_test_split(run_X, run_Y, stratify=run_Y, random_state=42)

print('Training...')
svc = SVC(kernel='rbf', C=1, gamma='auto')
svc.fit(X_train, y_train) 

print('Testing...')
print( "Accuracy on training set: {:.2f}".format(svc.score(X_train, y_train))) 
print( "Accuracy on test set: {:.2f}".format(svc.score(X_test, y_test ))) 


plt.boxplot( X_train , manage_xticks = False ) 
plt.yscale( "symlog" ) 
plt.xlabel( "Feature index" ) 
plt.ylabel ( "Feature magnitude" ) 
plt.savefig(r"feature_magnitude.png",bbox_inches='tight')

min_on_training=X_train.min(axis=0) 
print(min_on_training)

range_on_training = (X_train - min_on_training).max(axis = 0) 
print(range_on_training)


X_train_scaled = ( X_train - min_on_training ) / range_on_training 
X_test_scaled = ( X_test - min_on_training ) / range_on_training 
print("Minimum for each feature \n {}".format( X_train_scaled .min( axis = 0 ))) 
print ("Maximum for each feature \n {}".format( X_train_scaled.max( axis = 0 ))) 

print('Training...')
svc2 = SVC(kernel='rbf', C=1, gamma='auto') # change c to 10 for better fit
svc2.fit(X_train_scaled, y_train) 

print('Testing...')
print( "Accuracy on training set: {:.2f}".format(svc2.score(X_train_scaled, y_train))) 
print( "Accuracy on test set: {:.2f}".format(svc2.score(X_test_scaled, y_test ))) 

print(svc2.predict(data_X.reshape(1,-1)))
print(data_Y)



