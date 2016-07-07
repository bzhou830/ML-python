#!/usr/bin/env python
# coding=utf-8
# created by robin 

from math import log


#计算香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)                           #数据集合中的数据条数
    labelCounts = {}                                    #数据的标签数
    
    for featVec in dataSet:                             #遍历数据集合
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    
    shannonEnt = 0.0

    for key in labelCounts:                             #计算香农熵
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

#创建数据集合
def createDataSet():
    dataSet = [[1,1,'yes'],
              [1,1,'yes'],
              [1,0,'no'],
              [0,1,'no'],
              [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#测试香农熵计算函数
def test():
    myDat,labels = createDataSet()                      #创建一个数据集
    shnnon  = calcShannonEnt(myDat)                     #计算数据集合的香农熵
    print shnnon                                        #输出显示计算结果


#划分数据集
def splitDataSet(dataSet, aixs, value):
    retDataSet=[]                                       #返回数据集
    for featVec in dataSet:                             #遍历原来的数据集
        if featVec[aixs] == value:                      #
            reducedFeatVec = featVec[:aixs]             #
            reducedFeatVec.extend(featVec[aixs+1:])     #
            retDataSet.append(reducedFeatVec)           #
    return retDataSet                   


'''

'''


test()



