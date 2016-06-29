#!/usr/bin/env python
# coding=utf-8
import KNN
import numpy as np
import matplotlib.pyplot as plt


'''
datingDataMat,datingLabels = KNN.file2matrix('datingTestSet2.txt')

print datingDataMat,datingLabels

fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
          15.0 * np.array(datingLabels), 15.0 * np.array(datingLabels))
plt.show()
'''

KNN.datingClassTest();
