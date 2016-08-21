# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:21:48 2016

@author: pengcheng
"""

from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt

digits=load_digits()
X = digits.images.reshape((len(digits.images),-1))
y=digits.target

# Create the RFE object and rank each pixel
svc=SVC(kernel="linear",C=1)
rfe=RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
ranking=rfe.ranking_.reshape(digits.images[0].shape)

plt.matshow(ranking)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()

