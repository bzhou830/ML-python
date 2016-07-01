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

#KNN.datingClassTest()

def classifyPerson():
    print "输入相关信息"
    resultList = ['一点不喜欢','有点希望','可能性很大']
    percentTats = float(raw_input("玩游戏时间数目?"))
    ffMiles = float(raw_input("旅游公路数?"))
    ice = float(raw_input("冰淇淋消耗量?"))
    datingDataMat,datingLabels = KNN.file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = KNN.autoNorm(datingDataMat)
    inArr = np.array([ffMiles,percentTats,ice])
    classfierRt = KNN.classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print resultList[classfierRt - 1]


classifyPerson()

    
