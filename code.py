# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data = pd.read_csv(path)
#Code starts here

# Data Loading 
data=data.rename(columns={'Total':'Total_Medals'})
print(data.head(10))

print('='*80)

# Summer or Winter
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'], 'Both',
(np.where(data['Total_Summer']>data['Total_Winter'], 'Summer' , 'Winter')))
a=data['Better_Event'].value_counts()
better_event = list(a.keys())[0]
print(str(better_event))
print('='*80)

# Top 10
top_countries=data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
top_countries=top_countries.drop([146], axis=0)
def top_ten(df, col):
    country_list=[]
    top=df.nlargest(10, col)
    country_list=list(top['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries, 'Total_Summer')
top_10_winter=top_ten(top_countries, 'Total_Winter')
top_10=top_ten(top_countries, 'Total_Medals')
common=[]
for i in top_10_summer:
    if i in top_10_winter:
        if i in top_10:
            common.append(i)

print(common)

print('='*80)

# Plotting top 10
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
plt.figure(figsize=[14,8])
plt.xlabel("Name of the Country")
plt.ylabel("No of Total Summer Medals")
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.show()
plt.figure(figsize=[14,8])
plt.xlabel("Name of the Country")
plt.ylabel("No of Total Winter Medals")
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.show()
plt.figure(figsize=[14,8])
plt.xlabel("Name of the Country")
plt.ylabel("No of Total Medals")
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.show()

print('='*80)

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
s = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df['Golden_Ratio'].loc[s]
summer_country_gold = summer_df['Country_Name'].loc[s]
print(summer_country_gold," : ",summer_max_ratio)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
s = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df['Golden_Ratio'].loc[s]
winter_country_gold = winter_df['Country_Name'].loc[s]
print(winter_country_gold,' : ',winter_max_ratio)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
s = top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df['Golden_Ratio'].loc[s]
top_country_gold = top_df['Country_Name'].loc[s]
print(top_country_gold,' : ',top_max_ratio)

print('='*80)

# Best in the world 
data_1 = data.drop([146], axis=0)
data_1['Total_Points'] = (data_1['Gold_Total'] * 3) + (data_1['Silver_Total'] * 2) + data_1['Bronze_Total']
s = data_1['Total_Points'].idxmax()
most_points = data_1['Total_Points'].loc[s]
best_country = data_1['Country_Name'].loc[s]
print(best_country,' : ',most_points)

print('='*80)

# Plotting the best
best = data_1[data_1['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True, figsize=[10,8])
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


