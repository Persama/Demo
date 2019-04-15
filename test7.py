# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:06:16 2019

@author: afanx
"""
import dlib                     #人脸识别的库dlib
import numpy as np              #数据处理的库numpy
import cv2                      #图像处理的库OpenCv


class face_emotion():

    def __init__(self):
        # 使用特征提取器get_frontal_face_detector
        self.detector = dlib.get_frontal_face_detector()
        # dlib的68点模型，使用作者训练好的特征预测器
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        self.cnt = 0


    def learning_face(self):

        im_rd = cv2.imread('006.jpg')

        # 每帧数据延时1ms，延时为0读取的是静态帧
        k = cv2.waitKey(0)

        # 取灰度
        img_gray = cv2.cvtColor(im_rd, cv2.COLOR_RGB2GRAY)

        # 使用人脸检测器检测每一帧图像中的人脸。并返回人脸数rects
        faces = self.detector(img_gray, 0)

        # 待会要显示在屏幕上的字体
        font = cv2.FONT_HERSHEY_SIMPLEX

        # 如果检测到人脸
        if(len(faces)!=0):

            # 对每个人脸都标出68个特征点
            for i in range(len(faces)):
                # enumerate方法同时返回数据对象的索引和数据，k为索引，d为faces中的对象
                for k, d in enumerate(faces):
                    # 用红色矩形框出人脸
                    cv2.rectangle(im_rd, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255))
                    # 计算人脸热别框边长
                    self.face_width = d.right() - d.left()

                    # 使用预测器得到68点数据的坐标
                    shape = self.predictor(im_rd, d)
                    # 圆圈显示每个特征点
                    for i in range(68):
                        cv2.circle(im_rd, (shape.part(i).x, shape.part(i).y), 2, (0, 255, 0), -1, 8)
                        cv2.putText(im_rd, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.3,
                                    (255, 255, 255))
                        #print (str(i),shape.part(i).x, shape.part(i).y)
                        

            # 标出人脸数
            cv2.putText(im_rd, "Faces: "+str(len(faces)), (20,50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        else:
            # 没有检测到人脸
            cv2.putText(im_rd, "No Face", (20, 50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)

        # 添加说明
        #im_rd = cv2.putText(im_rd, "S: screenshot", (20, 400), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
        #im_rd = cv2.putText(im_rd, "Q: quit", (20, 450), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

        # 窗口显示
        cv2.imshow("camera", im_rd)
        cv2.waitKey(0)

if __name__ == "__main__":
    my_face = face_emotion()
    my_face.learning_face()

