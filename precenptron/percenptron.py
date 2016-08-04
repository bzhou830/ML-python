#__author__ = 'robin'
#coding = utf-8
import numpy as np
import matplotlib.pyplot as plt

class showPicture:
    def __init__(self,data,tag,w,b):
        self.b = b
        self.w = w
        plt.figure(1)
        plt.title('Pic', size=14)
        plt.xlabel('x', size=14)
        plt.ylabel('y', size=14)

        xData = np.linspace(0, 5, 100)
        yData = self.expression(xData)
        plt.plot(xData, yData, color='r', label='y1 data')
        for i in range(len(data)):
            if tag[i] == 1:
                plt.scatter(data[i][0],data[i][1],s=50)
            else:
                plt.scatter(data[i][0],data[i][1],marker='x',s=50)
        plt.savefig('pic.png',dpi=75)
    
    def expression(self,x):
        y = (-self.b - self.w[0]*x)/self.w[1]
        return y
    
    def show(self):
        plt.show()

class perceptron:
    def __init__(self,x,y,eta=1):
        self.x = x
        self.y = y
        self.w = np.zeros((x.shape[1],1))
        self.b = 0
        self.eta = eta
    
    def sign(self,w,b,x):
        y = np.dot(x,w)+b
        return int(y)
    
    def train(self):
        flag = True
        length = len(self.x)
        while flag:
            count = 0
            for i in range(length):
                #print self.x[i,:]
                tmpY = self.sign(self.w,self.b,self.x[i,:])
                if tmpY*self.y[i]<=0:
                    tmp = self.y[i] * self.eta * self.x[i,:]
                    tmp = tmp.reshape(self.w.shape)
                    self.w = self.w + tmp
                    self.b = self.b + self.eta * self.y[i]
                    count += 1
                    #print "ttt\n"
            if count == 0:
                flag = False
        return self.w,self.b

#
xArray = np.array([3,3,4,3,1,1])
xArray = xArray.reshape((3,2))
yArray = np.array([1,1,-1])

#
myPerceptron = perceptron(xArray,yArray,1)
w0,b0 = myPerceptron.train()

#
picture = showPicture(xArray,yArray,w=w0,b=b0)
picture.show()

