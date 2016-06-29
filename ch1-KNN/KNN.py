#!/usr/bin/env python
# coding=utf-8

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(inx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0] #样本集的个数
    diffMat=tile(inx,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)                 #打开文件
    arrayOfLines = fr.readlines()       #读取文件行数
    numberOfLines = len(arrayOfLines)   #文件行数
    returnMat=zeros((numberOfLines,3))  #矩阵
    classLabelVector = []               #标签
    index = 0                           
    for line in arrayOfLines:           
        line = line.strip() 
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals




