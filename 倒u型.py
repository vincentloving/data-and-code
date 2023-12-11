import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus']=False
dat=pd.read_excel("D:\\博文\\图数据.xlsx")
plt.rcParams['figure.dpi'] = 120
plt.figure(figsize=(12,6))
sns.barplot(x=dat["年份"],y=dat["投放量（万辆）"])
plt.xlabel('年份',fontsize=13)
plt.ylabel('投放量（万辆）',fontsize=13)
plt.title('共享电单车投放量柱形图',fontsize=16)
plt.xticks(rotation=70)

sns.barplot(x=dat["年份"],y=dat["市场规模（亿元）"])
plt.xlabel('年份',fontsize=13)
plt.ylabel('市场规模（亿元）',fontsize=13)
plt.title('共享电单车市场规模柱形图',fontsize=16)
plt.xticks(rotation=70)

df=pd.read_excel("D:\\期刊论文数据\\stata数据.xlsx")

# 假设我们有以下的数据点
x =df['digi']
y = df['green_d']
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
plt.scatter(x, y,color="black",s=10,label="gdev散点")
plt.plot(xm, func(xm,*popt),'--',color='red',label='倒U型拟合曲线')  # 'r'表示红色线条，代表拟合的曲线
plt.xlabel("gdev",fontsize=15)
plt.ylabel('dige',fontsize=15)
plt.legend()
plt.show()