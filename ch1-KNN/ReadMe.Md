# KNN

## 1. numpy
numpy是python的一个矩阵类型，提供大量的矩阵处理运算，numpy实际上包含了两种数据类型：
- 数组
- 矩阵

numpy模块中的tile函数

举例说明更好理解：
```
a[0,1,2]
b = tile(a,2)
```
这时候b的值为:
```
array([0,1,2,0,1,2])
```
这是个一维的。等同于使用
```
b=tile(a,(1,2))
```
如果想要使用二维的，那么就可以这样:
```
b=tile(a,[2,1])
```
这时候
```
array([0,1,2],
      [0,1,2])
```

![image](https://github.com/bzhou830/ML-python/raw/master/ch1-KNN/figure_1.png)


