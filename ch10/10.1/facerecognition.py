import cv2
import pandas as pd


def recognise_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(r'face_trainer/trainer.yml')
    cascadePath = r'C:\Users\llh\Anaconda3\envs\py36\Lib\site-packages'+\
                  '\cv2\data\haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_COMPLEX  # 设置字体
    people_list = pd.read_pickle('people_list.pkl')

    name_list = people_list.name.tolist()
    id_list = people_list.id.tolist()

    cam = cv2.VideoCapture(0)
    minW = cam.get(3)  # 获取视频流的宽度
    minH = cam.get(4)  # 获取视频流的高度

    while True:
        # 按帧读取视频，如果为组后一帧ret为False，否则ret为True，img为每一帧的图片
        ret, img = cam.read()
        # 将图片转化为灰度
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 调用分类器对象
        faces = faceCascade.detectMultiScale(
            gray,  # 要检测的输入图像
            scaleFactor=1.2,  # 表示每次图像尺寸减小的比例
            minNeighbors=5,  # 表示一个目标被检测到多少次才算是真正的人脸
            minSize=(int(0.1 * minW), int(0.1 * minH))  # 目标的最小尺寸
        )
        cv2.putText(img, 'Press ESC to exit', (5, 20), font, 0.6, (0, 0, 255), 1)
        # x、y代表人脸图像左上角，w、h代表人脸图像的宽和高
        for (x, y, w, h) in faces:
            # 在图像上绘制一个矩形
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # 使用识别器识别检测到的人脸，其中id代表识别的序号，confidence代表置信度
            id, confidence = recognizer.predict(
                gray[y:y + h, x:x + w])
            name = name_list[id_list.index(str(id))]
            print('\b' * 20, end='')
            print('This is', name, end='', flush=True)
            cv2.putText(img, 'This is ' + str(name),
                        (x + 5, y - 5), font, 1, (0, 0, 255), 2)

        cv2.imshow('recognition', img)
        k = cv2.waitKey(10)
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    recognise_face()
