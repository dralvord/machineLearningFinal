import sys
sys.path.append('/home/ubuntu/workspace/utils')

import mglearn as mglearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


run_X = np.genfromtxt('SpringSplit_X.csv', unpack = False, delimiter = ',')
run_Y = np.genfromtxt('SpringSplit_Y.csv', unpack = False, delimiter = ',')


# split the data into a training sert and a testing set

X_train , X_test , y_train , y_test = train_test_split(run_X, run_Y, stratify=run_Y, random_state=42)
print('X_train shape: {}'.format(X_train.shape))
print('y_train shape: {}'.format(y_train.shape))
print('X_test shape: {}'.format(X_test.shape))
print('y_test shape: {}'.format(y_test.shape))


#plt.boxplot( X_train , manage_xticks = False ) 
plt.yscale( "symlog" ) 
plt.xlabel( "Feature index" ) 
plt.ylabel ( "Feature magnitude" ) 
#plt.savefig(r"feature_magnitude.png",bbox_inches='tight')