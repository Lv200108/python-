import numpy as np
from PIL import Image
import os
import cv2


# 获取人脸和对应的id
def get_face_and_id(path):
    # 获取所有人脸图片的路径
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    # 获取用于人脸检测的haar分类器
    detector = cv2.CascadeClassifier(
        r'C:\\Users\llh\Anaconda3\envs\py36\Lib\site-packages' +
        '\cv2\data\haarcascade_frontalface_default.xml')
    for imagePath in imagePaths:
        # 转化为灰度
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        # 检测出图片中的人脸
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x: x + w])
            ids.append(id)
    return faceSamples, ids


def train_recognizer():
    # 人脸数据路径
    path = r'C:/Users/llh/PycharmProjects/example_in_book/Face_detection/Facedate/'
    # 基于LBP算法的人脸识别器
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    print('正在训练，稍等片刻......')
    faces, ids = get_face_and_id(path)
    # 训练人脸识别器
    recognizer.train(faces, np.array(ids))
    # 保存模型
    recognizer.write(r'face_trainer\trainer.yml')
    print("{0} 张人脸被训练，正在退出训练人脸识别器训练环节......".format(len(np.unique(ids))))


if __name__ == '__main__':
    train_recognizer()
