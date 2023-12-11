import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['figure.dpi'] = 120
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus']=False


df=pd.read_excel("D:\\期刊论文数据\\总数据data.xlsx")

# 假设我们有以下的数据点
x =df['dige']
y = df['gdev']
from scipy.optimize import curve_fit
# 定义二次多项式
def func(x, a, b, c):
    return a * x**2 + b * x + c

# 生成散点图
plt.scatter(x, y)
plt.show()
# 使用curve_fit进行拟合，获取拟合参数a, b, c
def replace_invalid_numbers(arr, value=0):
    invalid = np.isinf(arr) | np.isnan(arr)
    arr[invalid] = value
    return arr

replace_invalid_numbers(x)
replace_invalid_numbers(y)

popt,pcov = curve_fit(func, x, y)

print("拟合参数: ", popt)
# 使用拟合参数绘制二次曲线
xm=pd.Series(range(1,101))/100
plt.figure(figsize=(10,5))
plt.scatter(x, y,color="black",s=10,label="Gdev scatters")
plt.plot(xm, func(xm,*popt),'--',color='red',label='Inverted U-shaped fitting curve')  # 'r'表示红色线条，代表拟合的曲线
plt.xlabel("Gdev",fontsize=15)
plt.ylabel('Dige',fontsize=15)
plt.legend(loc='upper right')
plt.show()