import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def regress(x,y,a,b):
    #regression line y=a+bx
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    y_pred=a+b*x
    plt.plot(x,y_pred, color="r")
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()


def main():
    x = np.array([17, 13, 12, 15, 16,14, 16, 16, 18, 19])
    y = np.array([94, 73, 59, 80, 93, 85, 66, 79, 77, 91])
    #to store vectors
    x_bar=[]
    y_bar=[]
    xy_bar=[]
    x_sq=[]
    y_sq=[]
    meanx = np.mean(x)
    meany = np.mean(y)
    print(meanx)
    print(meany)
    for i in range(0,10):
        x_bar.append(x[i]-meanx)
    print(x_bar)
    avg_x=sum(x_bar)/10
    print(avg_x)
    for j in range(0,10):
        y_bar.append(y[j]-meany)
    print(y_bar)
    avg_y=sum(y_bar)/10
    print(avg_y)
    for i in range(0,10):
        xy_bar.append((x[i]-meanx)*(y[i]-meany))
    print(xy_bar)
    avg_xy=sum(xy_bar)
    print(avg_xy)

    for i in range(0,10):
        x_sq.append((x_bar[i]**2))
    print(x_sq)
    avg_xsq=sum(x_sq)
    print(avg_xsq)

    for i in range(0,10):
        y_sq.append((y_bar[i]**2))
    print(y_sq)
    avg_ysq=sum(y_sq)
    print(avg_ysq)
#pearson correlation coefficient
    r=avg_xy/(sqrt(avg_xsq*avg_ysq))
    print(r)
#calculate coefficient
#sy=sqrt((sum(y-ybar)^2)/n-1))
    sy=sqrt((avg_ysq)/9)
    sx=sqrt((avg_xsq)/9)
    print("\n")
    print(sy)
    print(sx)
#calculate slope
    b=r*(sy/sx)
    print(b)
#calculate y-intercept
    a=meany-(b*meanx)
    print(a)
    regress(x,y,a,b)
 

    


if __name__ == "__main__":
    main()


    
 
