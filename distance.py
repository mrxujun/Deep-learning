# -- coding:utf-8 --
#球面距离 两个点之间的距离并不是在一条直线上
#余弦距离 Cosine Distance  两个向量之间的夹角，夹角越小，距离越近，他们的偏好相同
#欧几里得距离 Euclidean Distance 两个点之间的距离
#曼哈顿距离 Manhattan distance 街区距离
import math
#球面距离
def geo_distance(origin, destination) :

    lon1, lat1=origin
    lon2, lat2=destination
    radius=6371  # km 地球半径

    dlat=math.radians(lat2 - lat1)
    dlon=math.radians(lon2 - lon1)
    a=(math.sin(dlat / 2) * math.sin(dlat / 2) +
       math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
       math.sin(dlon / 2) * math.sin(dlon / 2))
    c=2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d=radius * c
    return d

# 余弦距离
import numpy as np
def cos_distance(origin,destination):
    distance = 1-np.dot(origin,destination)/np.linalg.norm(origin) * np.linalg.norm(destination)
    return distance
print(cos_distance([3,4],[2,1]))

# 欧几里得距离
def euc_distance(orgin,destination):
    distance = np.linalg.norm(np.array(orgin)-destination)
    return distance
#曼哈顿距离
def man_distance(origin,destination):
    distance = sum(abs(np.array(origin)-destination))
    return distance

