import pandas as pd
import numpy as np
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


def LinearRecursionOnPandas(df):
    datapoints=[]
    percentageSums=[]
    rowLengths=[]
    for i in range(12,24):
        percentageSums.append(df[f"totRevenue_{str(i)}"].sum(skipna=True))
        rowLengths.append(df[f"totRevenue_{str(i)}"].count())
    # print(df.isin([np.inf]).sum())
    # print(percentageSums)
    # print()
    # print(rowLengths)
    Y=[percentageSums[i]/rowLengths[i] for i in range(len(percentageSums))]
    datapoints=[[2000+(i),Y[i-12]] for i in range(12,24)]
    cubicSplineOnData(datapoints)
    return datapoints


def cubicSplineOnData(data):
    x=[data[i][0] for i in range(len(data))]
    y=[data[i][1] for i in range(len(data))]

    cs = CubicSpline(x, y)

    x_new = np.linspace(1, 5, 100)
    y_new = cs(x_new)

    plt.scatter(x, y, color='blue')
    plt.plot(x_new, y_new, color='red')
    plt.show()



# def linearRecursion(Y):
#     X=[i+1 for i in range(len(Y))]
#     X1 = np.vstack([X, np.ones(len(X))]).T  # Add the bias term (intercept)
#     # Perform linear regression using least squares
#     slope, intercept = np.linalg.lstsq(X1, Y, rcond=None)[0]
#     return [[2000+(i/10.0),(slope*(i/10.0))+intercept] for i in range(12*10,23*10)]

