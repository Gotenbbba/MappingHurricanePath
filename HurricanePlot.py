import numpy as np # 导入 numpy 模块，用于处理数组和矩阵
import matplotlib.pyplot as plt # 导入 matplotlib.pyplot 模块，用于绘制图形
from mpl_toolkits.basemap import Basemap # 导入 Basemap 模块，用于绘制地图
from netCDF4 import Dataset # 导入 Dataset 模块，用于读取 netCDF 格式的数据

def readtopo(dir): # 定义一个函数，用于读取地形数据
    data = Dataset(dir) # 读取数据文件
    lon = data.variables['lon'][:] # 获取经度数据
    lat = data.variables['lat'][:] # 获取纬度数据
    topo = data.variables['topo'][:] # 获取地形高度数据
    return lon, lat, topo # 返回经度、纬度和地形高度

dir = 'ETOPO1_Ice_g_gmt4.grd' # 定义数据文件的路径
lon, lat, topo = readtopo(dir) # 调用函数，读取数据

fig = plt.figure(figsize=(10, 7)) # 创建一个图形对象，并设置大小
ax = fig.add_subplot(111) # 添加一个子图

m = Basemap(projection='merc', llcrnrlat=0, urcrnrlat=50, llcrnrlon=-120, urcrnrlon=-30, resolution='l') # 创建一个墨卡托投影的地图对象，并设置范围和分辨率
m.drawcoastlines() # 绘制海岸线
m.drawcountries() # 绘制国界线
m.drawstates() # 绘制州界线
m.drawmapboundary(fill_color='aqua') # 绘制地图边界，并填充颜色为水色
m.fillcontinents(color='coral', lake_color='aqua') # 填充大陆颜色为珊瑚色，湖泊颜色为水色

x, y = m(lon, lat) # 将经纬度转换为地图上的坐标
cs = m.contourf(x, y, topo, cmap=plt.cm.jet) # 绘制地形高度的等值线，并使用彩虹色彩表
cb = m.colorbar(cs, location='right', pad='5%') # 添加颜色条，并设置位置和间距
cb.set_label('Elevation (m)') # 设置颜色条的标签

data = np.loadtxt('hurricane.csv', delimiter=',', skiprows=1) # 读取飓风路径数据，跳过第一行表头
lon = data[:, 2] # 获取经度数据
lat = data[:, 3] # 获取纬度数据
wind = data[:, 4] # 获取风速数据

x, y = m(lon, lat) # 将经纬度转换为地图上的坐标
m.plot(x, y, color='k', linewidth=2, label='Katrina') # 绘制飓风路径，并设置颜色、线宽和标签
m.scatter(x, y, c=wind, cmap=plt.cm.coolwarm) # 绘制飓风位置，并根据风速设置颜色，使用冷暖色彩表

plt.title('Track of Hurricane(2020)') # 设置图像标题
plt.legend(loc='lower left') # 显示图例，并设置位置为左下角
plt.show() # 显示图像
