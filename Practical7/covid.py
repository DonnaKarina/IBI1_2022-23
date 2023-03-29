import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('/Users/hanhan')
covid_data = pd.read_csv('full_data.csv')
covid_data.head(5)
covid_data.head(7)
covid_data.info()
print(covid_data.describe ())
covid_data.iloc[0,1]
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
covid_data.iloc[0:1001:100,1]
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
covid_data.loc[2:4,'date']
covid_data.loc[0:81,'total_cases']
#TA told me how to search in the rows
covid_data.loc[covid_data.loc[:,'location'] == 'Afghanistan','total_cases']
my_columns = [False, True, True, True, False, False]
new_data = covid_data.loc[covid_data.loc[:,'date']=='2020-03-31',my_columns]
print(new_data)
temp=new_data.iloc[:,1:3]
#how to use numpy is learnt from https://blog.csdn.net/u013250861/article/details/123965146?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-0-123965146-blog-122905081.235^v27^pc_relevant_3mothn_strategy_recovery&spm=1001.2101.3001.4242.1&utm_relevant_index=2
np.mean(temp,axis=0)
#the new cases are more than the new deaths
#use index to represent the mean and calculate the proportion
a=np.mean(temp,axis=0)[0]
b=np.mean(temp,axis=0)[1]
proportion=b/a
print(proportion)
#now make the boxplot
new_data.info()
c=new_data.loc[:,'new_cases']
fig=plt.figure()
view=plt.boxplot(c)
plt.show()
#reinstall my spyder by https://blog.csdn.net/mjr212/article/details/113794872
d=new_data.loc[:,'new_deaths']
fig=plt.figure()
view=plt.boxplot(d)
plt.show()
world_dates=covid_data.loc[covid_data.loc[:,'location'] == 'World','date']
world_new_cases=covid_data.loc[covid_data.loc[:,'location'] == 'World','new_cases']
plt.plot(world_dates, world_new_cases,'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
