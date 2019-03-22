# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
condition_1=data['Total_Summer']>data['Total_Winter']
condition_2=data['Total_Summer']==data['Total_Winter']
data['Better_Event']=np.where(condition_1, 'Summer',(np.where(condition_2, 'Both', 'Winter')))
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)




# --------------
#Code starts here




top_countries= data.filter(['Country_Name','Total_Summer', 'Total_Winter','Total_Medals'], axis=1)
top_countries.drop(index=len(top_countries)-1,axis=0,inplace=True)

def top_ten(top_countries,column):
    l=top_countries.nlargest(10,column)
    country_list=list(l['Country_Name'])
    return country_list
top_10_summer=top_ten(top_countries,"Total_Summer")
top_10_winter=top_ten(top_countries,"Total_Winter")
top_10=top_ten(top_countries,"Total_Medals")

print(top_10_summer)
print(top_10_winter)
print(top_10)
common=[x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)


# --------------
#Code starts here
summer_df=data[data["Country_Name"].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]
fig, (ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))

summer_df.plot(kind='bar',ax=ax_1)
winter_df.plot(kind='bar',ax=ax_2)
top_df.plot(kind='bar',ax=ax_3)


# --------------
#Code starts here

#for summer
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
c1=summer_df.loc[summer_df['Golden_Ratio'] == summer_max_ratio]
summer_country_gold=c1.iloc[0]["Country_Name"]
print(summer_country_gold)

#for winter
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
c2=winter_df.loc[winter_df['Golden_Ratio'] == winter_max_ratio]
winter_country_gold=c2.iloc[0]["Country_Name"]
print(winter_country_gold)
#for total
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
c3=top_df.loc[top_df['Golden_Ratio'] == top_max_ratio]
top_country_gold=c3.iloc[0]["Country_Name"]
print(top_country_gold)



# --------------
#Code starts here
data_1=data.drop(index=len(data)-1,axis=0)
#update
data_1['Total_Points']=data_1['Gold_Total']*3+data_1['Silver_Total']*2+data_1['Bronze_Total']
most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print("THE BEST COUNTRY IS:",best_country,"WITH",most_points,"POINTS")


# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot(kind='bar', stacked=True, figsize=(15,10))
plt.xlabel("United States")
plt.ylabel("Medals")
plt.xticks(rotation=45)


