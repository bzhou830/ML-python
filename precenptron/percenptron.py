#__author__ = 'robin'
#coding = utf-8
import numpy as np
import matplotlib.pyplot as plt

class showPicture:
    def __init__(self,data,w,b):
        self.b = b
        self.w = w
        plt.figure(1)
        plt.title('Plot 1', size=14)
        plt.xlabel('x-axis', size=14)
        plt.ylabel('y-axis', size=14)

        xData = np.linspace(0, 5, 100)
        yData = self.expression(xData)
        plt.plot(xData, yData, color='r', label='y1 data')

        plt.scatter(data[0][0],data[0][1],s=50)
        plt.scatter(data[1][0],data[1][1],s=50)
        plt.scatter(data[2][0],data[2][1],marker='x',s=50,)
        plt.scatter(data[3][0],data[3][1],marker='x',s=50,)
        plt.savefig('2d.png',dpi=75)
    
    def expression(self,x):
        y = (-self.b - self.w[0]*x)/self.w[1]
        return y
    
    def show(self):
        plt.show()

class perceptron:
    def __init__(self,x,y,a=1):
        self.x = x
        self.y = y
        self.w = np.zeros((x.shape[1],1))
        self.b = 0
        self.a = 1
    
    def sign(self,w,b,x):
        result = 0
        y = np.dot(x,w)+b
        return int(y)
    
    def train(self):
        flag = True
        length = len(self.x)
        while flag:
            count = 0
            for i in range(length):
                tmpY = self.sign(self.w,self.b,self.x[i,:])
                if tmpY*self.y[i]<=0:
                    tmp = self.y[i]*self.a*self.x[i,:]
                    tmp = tmp.reshape(self.w.shape)
                    self.w = tmp +self.w
                    self.b = self.b + self.y[i]
                    count +=1
            if count == 0:
                flag = False
        return self.w,self.b

#
#data = [[3,3],[4,3],[1,1]]
xArray = np.array([3,3,4,3,1,1,2,0])
xArray = xArray.reshape((4,2))
yArray = np.array([1,1,-1,-1])

#
myPerceptron = perceptron(x=xArray,y=yArray)
weight,bias = myPerceptron.train()

#
picture = showPicture(xArray,w=weight,b=bias)
picture.show()

