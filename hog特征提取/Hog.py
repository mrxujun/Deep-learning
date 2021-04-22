# -- coding:utf-8 --
import math
import os

import cv2
import generateData
import numpy as np
from scipy.interpolate import lagrange

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
class Hog_descriptor():
    def __init__(self,img,cell_size = 2,bin_size = 2):
        self.img = img
        self.cell_size = cell_size
        self.bin_size = bin_size
        self.angle_unit = 360 / bin_size

    # hog特征提取

    # 计算像素的梯度
    def exact_feature(self):
        gradient_x = cv2.Sobel(self.img,cv2.CV_32F,1,0,ksize=3)
        gradient_y = cv2.Sobel(self.img,cv2.CV_32F,0, 1, ksize=3)
        gradient_magnitude=np.sqrt(gradient_x** 2 + gradient_y ** 2)
        gradient_angle = cv2.phase(gradient_x, gradient_y, angleInDegrees=True)
        return gradient_magnitude,gradient_angle

    #计算cell的梯度直方图
    def cell_gradient(self,cell_magnitude,cell_angle):
        orientation_level = [0] * self.bin_size
        for i in range(cell_magnitude.shape[0]):
            for j in range(cell_magnitude.shape[1]):
                gradient_strength = cell_magnitude[i][j]
                gradient_angle = cell_angle[i][j]
                id_0 = int(gradient_angle / self.angle_unit)
                mod = gradient_angle % self.angle_unit
                id_1 = (id_0 + 1) % self.bin_size
                orientation_level[id_0] += gradient_strength * (1-mod / self.angle_unit)
                orientation_level[id_1] += gradient_strength * (mod / self.angle_unit)
        return orientation_level

    def extract(self):
        height,width = self.img.shape
        gradient_magnitude,gradient_angle = self.exact_feature()
        gradient_angle = abs(gradient_angle)
        cell_gradient_vector = np.zeros((height//self.cell_size,width//self.cell_size,self.bin_size))
        # print(cell_gradient_vector)
        for i in range(cell_gradient_vector.shape[0]):
            for j in range(cell_gradient_vector.shape[1]):
                cell_magnitude = gradient_magnitude[i*self.cell_size:(i+1)*self.cell_size,j*self.cell_size:(j+1)*self.cell_size]
                cell_angle = gradient_angle[i*self.cell_size:(i+1)*self.cell_size,j*self.cell_size:(j+1)*self.cell_size]
                cell_gradient_vector[i][j] =self.cell_gradient(cell_magnitude,cell_angle)

        hog_image=self.render_gradient(np.zeros([height, width]), cell_gradient_vector)
        hog_vector=[]
        for i in range(0,cell_gradient_vector.shape[0]-1):
            for j in range(0,cell_gradient_vector.shape[1]-1):
                # 4个cell得到一个block
                block_vector=cell_gradient_vector[i:i+2,j:j+2,:].reshape(-1,1)
                # 正则化
                block_vector = np.squeeze(block_vector)
                # block_vector=np.array([vector / np.linalg.norm(vector) for vector in block_vector])
                block_vector=np.linalg.norm(block_vector)
                hog_vector.append(block_vector)
        hog_vector = np.linalg.norm(hog_vector)
        return hog_vector,hog_image

    def render_gradient(self,image,cell_gradient):
        cell_width = self.cell_size/ 2
        max_mag = np.array(cell_gradient).max()
        for x in range(cell_gradient.shape[0]):
            for y in range(cell_gradient.shape[1]):
                cell_grad = cell_gradient[x][y]
                cell_grad /= max_mag
                angle = 0
                angle_gap = self.angle_unit
                for magnitude in cell_grad:
                    angle_radian = math.radians(angle)
                    angle_radian = math.radians(angle)
                    x1 = int(x * self.cell_size + magnitude * cell_width * math.cos(angle_radian))
                    y1 = int(y * self.cell_size + magnitude * cell_width * math.sin(angle_radian))
                    x2 = int(x * self.cell_size - magnitude * cell_width * math.cos(angle_radian))
                    y2 = int(y * self.cell_size - magnitude * cell_width * math.sin(angle_radian))
                    cv2.line(image, (y1, x1), (y2, x2), int(255 * math.sqrt(magnitude)))
                    angle += angle_gap
        return image

    #拉格朗日拟合函数曲线
    def f(self):
        x = [3.5, 3.32, 3.21, 3.35, 2.39, 2.37, 3.85, 3.13, 2.77, 3.01]
        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        f = lagrange(x, y)
        return f


if __name__ == "__main__" :

    image_data = generateData.generate_image()
    print("对每张图片进行识别")
    for i in range(0, 10) :
        x = image_data[i]
        x = x.numpy()
        hog = Hog_descriptor(x, cell_size=2, bin_size=2)
        vector,image = hog.extract()
        vector = round(vector,2)
        # 对提取到得特征进行分类
        result = int(round(hog.f()(vector), 2))
        # 打印出分类结果
        print("图像[%s]得分类结果是:[%s],它得特征是[%s]" % (i, result, vector))