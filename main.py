# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:19:52 2022

@author: 88697
"""

import random 
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np
def fun0(w,a,b):
    h=[a[i]*w[0]+w[1]*b[i]+w[2] for i in range(len(a))]
    list1=[]
    for i in h:
        if i>0:
            list1.append(1)
        elif i<0:
            list1.append(-1)
        else:
            list1.append(0)
    return np.array(list1)
def pltfun(w,l,color='b'):
    if w[1]!=0:
        x=[i for i in range(-30,30,1) ]
        y=[(i*w[0])+w[2]/-w[1] for i in x]
    else: 
        x=[-w[2]/w[0] for i in range(0,3,1)]
        y=[0,-10,10]
    if w[0]==w0[0] and w[1]==w0[1] and w[2]==w0[2]:
        return plt.plot(x,y,color='r',label=l)
    else:
        return plt.plot(x,y,color,label=l)
k=1000
k1=100
x=np.array([random.normalvariate(5,10) for _ in range(k)])
y=np.array([random.normalvariate(5,10) for _ in range(k)])
x1=np.array([random.normalvariate(-5,20) for _ in range(k1)])
y1=np.array([random.normalvariate(-5,20) for _ in range(k1)])
w0=[5.3,4.4,-4.2]
plt.scatter(x1,y1,s=0,color='g')
x0=[-31,0,31]
y0=[0,0,0]
l_label=fun0(w0,x,y)
ll_label=fun0(w0,x1,y1)
red=l_label>0
blue=l_label<0
plt.scatter(x[red],y[red],s=5,color='r')
plt.scatter(x[blue],y[blue],s=5,color='b')
plt.plot(x0,y0,color='k',linestyle=':')
plt.plot(y0,x0,color='k',linestyle=':')
plt.xlim(-30,30)
plt.ylim(-30,30)

c=[1 for i in range(k)]
c1=[1 for i in range(k1)]
z=list(zip(x,y,c,l_label))
z1=list(zip(x1,y1,c1,ll_label))
pltfun(w0,l='answer')
w=[3,-1,1]
pltfun(w,color='y',l='first')     
for _ in range(50):
  random.shuffle(z)
  for i in z:
    pp=(i[0]*w[0]+i[1]*w[1]+i[2]*w[2])*i[3]
    if pp<0:
       w=[w[0]+i[3]*i[0],w[1]+i[3]*i[1],w[2]+i[3]*i[2]]
    else:
        continue
predicted_label=fun0(w,x1,y1)
acc_label=[1 for i in range(len(predicted_label)) if ll_label[i]==predicted_label[i]]

print('Perceptron accuary :%.3f' % (len(acc_label)/len(predicted_label)))
pltfun(w,color='g',l='predict')
plt.title('shuffle')
plt.legend()
plt.show()
################################比較SVM
svclassifier=SVC(kernel='linear')
X_train=list(zip(x,y))
Y_train=l_label
svclassifier.fit(X_train,Y_train)
X_test=list(zip(x1,y1))
Y_test=np.array(ll_label)
Y_predicted=svclassifier.predict(X_test)
accuracy=sum([1  for i in range(50) if Y_predicted[i]==Y_test[i]])/50
print("SVM accuary: %.3f"%accuracy)
