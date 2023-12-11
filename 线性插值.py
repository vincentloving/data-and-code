import pandas as pd
# 读取截面数据
df =pd.read_excel('进出口贸易.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2022):
        Year = str(year)
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'province',1:'year',2:'进出口贸易总额'})
df1.to_excel('进出口贸易总额.xlsx',index = False)

#环境支出
df =pd.read_excel('环境支出.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2022):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'省份',1:'年份',2:'环境支出'})
df1.to_excel('gdp_panel.xlsx',index = False)

nd=pd.read_excel("环境支出_处理后.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

nd=pd.read_excel("电力消费量_处理后.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

#绿色全要素
nd=pd.read_excel("绿色全要素生产率.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

##专利
df =pd.read_excel('专利.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2022):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'省份',1:'年份',2:'国内三种专利有效数合计（件）'})
df1.to_excel('gdp_panel.xlsx',index = False)

#插值
nd=pd.read_excel("专利_面板.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

#CGI
nd=pd.read_excel("CGI.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

##人口密度
df =pd.read_excel('人口密度.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2022):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'省份',1:'年份',2:'人口密度'})
df1.to_excel('gdp_panel.xlsx',index = False)

nd=pd.read_excel("人口密度_面板.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

##R&D
df =pd.read_excel('RD.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2022):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'省份',1:'年份',2:'R&D'})
df1.to_excel('R&D.xlsx',index = False)

#插值
nd=pd.read_excel("R&D.xlsx")
nd1=nd.interpolate()
nd1.to_excel('nd.xlsx',index=False)

#工业固体废物
df =pd.read_excel('废物利用率_面板.xlsx')
df
df1=df.interpolate()
df1.to_excel('废物利用率_填充.xlsx')

df =pd.read_excel('外商投资.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2023):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'province',1:'year',2:'外商投资'})
df1.to_excel('gdp_panel.xlsx',index = False)

df =pd.read_excel('财政总支出.xlsx')
df

list1 = []
for index in range(0,df.shape[0]):
    city = df.at[index,'地区']
    for year in range(2013,2023):
        Year = str(year)+'年'
        gdp = df.at[index,Year]
        list1.append([city,year,gdp])

df1 = pd.DataFrame(list1)
df1 = df1.rename(columns={0:'province',1:'year',2:'财政总支出'})
df1.to_excel('财政.xlsx',index = False)

