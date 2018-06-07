import numpy as np
import matplotlib.pyplot as plt


#input data
x=np.array([[-2,4,-1],[4,1,-1],[1,6,-1],[2,4,-1],[6,2,-1]])

#assign labels
y=np.array([-1,-1,1,1,1])


def svm_plot(X,Y):
    w=np.zeros(len(X[0]))
    print(w)
    #learning rate
    lr=0.71
    #no.of iteration
    epochs=100000
    errors= []
    for epoch in range(1, epochs):
        error= 0
        for i ,a in enumerate(x):
            if(Y[i]*np.dot(X[i],w)) < 1:
                w=w + lr * ((X[i] * Y[i]) + (-2*(1/epoch) * w))
                error=1
            else:
                w=w+lr*(-2*(1/epoch)*w)
        errors.append(error)
    print(w)
    return w


w=svm_plot(x , y)


for d,sample in enumerate(x):
    if d < 2:
        plt.scatter(sample[0],sample[1], s=100,marker='_', linewidths=2)
    else:
        plt.scatter(sample[0],sample[1], s=100,marker="+", linewidths=2)

#plt.plot([-2,6],[6,0.5])
#plt.show()

#Testing dataset
plt.scatter(2,2, s=100,marker='_',linewidths=2, color="yellow")
plt.scatter(4,3, s=100,marker='+',linewidths=2, color="blue")
plt.scatter(1,2, s=100,marker='_',linewidths=2, color="black")
plt.scatter(5,4, s=100,marker='+',linewidths=2, color="orange")


x2=[w[0],w[1],-w[1],w[0]]
x3=[w[0],w[1],w[1],-w[0]]
print(x2)
print(x3)
x2x3=np.array([x2,x3])
print(x2x3)
X,Y,U,V=zip(*x2x3)
print("\n")
print(U)
print(V)
print(X)
print(Y)
#fig=plt.figure()
#ax=fig.add_subplot(111)
ax=plt.gca()
ax.quiver(X, Y, U,V,scale=1,color="green")
plt.show()


















