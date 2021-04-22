# -- coding:utf-8 --
import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
def generate_image():
    image_label=[]
    num_0=tf.constant(
        [[0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_1=tf.constant(
        [[0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_2=tf.constant(
        [[0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_3=tf.constant(
        [[0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_4=tf.constant(
        [[0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_5=tf.constant(
        [[0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )

    num_6=tf.constant(
        [[0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_7=tf.constant(
        [[0, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_8=tf.constant(
        [[0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    num_9=tf.constant(
        [[0, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0]], tf.float32
    )
    image_label.append(num_0)
    image_label.append(num_1)
    image_label.append(num_2)
    image_label.append(num_3)
    image_label.append(num_4)
    image_label.append(num_5)
    image_label.append(num_6)
    image_label.append(num_7)
    image_label.append(num_8)
    image_label.append(num_9)
    return image_label

