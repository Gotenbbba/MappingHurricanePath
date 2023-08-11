import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
fig=plt.figure(figsize=(10,7))
ax=plt.axes(projection=ccrs.PlateCarree())
box=[100,180,0,40]
xstep,ystep=10,5
ax.set_extent(box,crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.coastlines('50m')
ax.set_xticks(np.arange(box[0],box[1]+xstep,xstep),crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(box[2],box[3]+ystep,ystep),crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
plt.tick_params(labelsize=18)
year=input('输入年份, enter the year：')
filename='table'+year+'.csv'
DATA=pd.read_csv(filename)
data=DATA.values
ylist=[[]]
xlist=[[]]
vlist=[[]]
length=np.shape(data)[0]
for i in range(1,length):
    if str(data[i-1,4])[2]=='0':
        index=eval(str(data[i-1,4])[-1])-1
    else:
        index=eval(str(data[i-1,4])[2:])-1
    if data[i,4]==data[i-1,4]:
        ylist[index].append(data[i,7])
        xlist[index].append(data[i,8])
        vlist[index].append(data[i,10])
    else:
        ylist.append([])
        xlist.append([])
        vlist.append([])
for i in range(index+1):
    ax.plot(xlist[i],ylist[i],c='black',alpha=1,linewidth=1.5,label='Marie')#开始连线
    as1=ax.scatter(xlist[i],ylist[i],s=30,marker='o',c=vlist[i],zorder=3,cmap='Reds')#zorder改变图层顺序
title='Track of Tropical Cyclone in N.W. Pacific in '+year
plt.title(title,fontsize=20)
figurename='TyphoonPathIn'+year+'.jpg'
plt.savefig(figurename)