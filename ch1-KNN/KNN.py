#!/usr/bin/env python
# coding=utf-8

from numpy import *
import operator


def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


'''
inx         输入向量
dataSet     训练数据集
labels      训练数据集标签
k           最临近数目
'''
def classify0(inx,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]                                    #样本集的个数
    diffMat=tile(inx,(dataSetSize,1)) - dataSet                     #矩阵之差
    sqDiffMat = diffMat**2                                          #矩阵之差的平方
    sqDistances=sqDiffMat.sum(axis=1)                               #矩阵的每一行相加，得到一个向量  
    distances=sqDistances**0.5                                      #向量的长度
    sortedDistIndicies = distances.argsort()                        #数组从小到大的索引值
    classCount={}                                                   #类统计
    for i in range(k):                                              #最临近数目
        voteIlabel = labels[sortedDistIndicies[i]]                  #最临近数的标签
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1   #统计标签个数
    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),reverse=True)#排序
    return sortedClassCount[0][0]                                   #返回数量最多的标签


def file2matrix(filename):
    fr = open(filename)                                             #打开文件
    arrayOfLines = fr.readlines()                                   #读取文件行数
    numberOfLines = len(arrayOfLines)                               #文件行数
    returnMat=zeros((numberOfLines,3))                              #矩阵
    classLabelVector = []                                           #标签
    index = 0                           
    for line in arrayOfLines:           
        line = line.strip() 
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

'''
dataSet 传入矩阵数据集
normDataSet 返回归一化后数据集
ranges 
minVals 
'''
def autoNorm(dataSet):
    minVals = dataSet.min(0)                                        #
    maxVals = dataSet.max(0)                                        #
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return normDataSet,ranges,minVals


def datingClassTest():
    hoRatio = 0.20                                                  #测试数据集所占比例
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')  #加载数据
    normMat, ranges, minVals = autoNorm(datingDataMat)              #归一化数据
    m = normMat.shape[0]                                            
    numTestVecs = int(m*hoRatio)                                    #测试数数量
    errorcount = 0.0
    for i in range(numTestVecs):                                    #
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "Rt is %d, Real is %d" % (classifierResult,datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorcount += 1.0

    print " %f " % (errorcount/float(numTestVecs))



