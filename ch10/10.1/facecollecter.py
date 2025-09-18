import os
import cv2
import pandas as pd


def collect_face_data():
    # 判断当前目录下是否存有名单，没有则创建
    if os.path.exists(r'people_list.pkl'):
        people_list = pd.read_pickle(r'people_list.pkl')
    else:
        people_list = pd.DataFrame({'id': [], 'name': []})
    # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
    cap = cv2.VideoCapture(0)
    # 字体设置
    font = cv2.FONT_HERSHEY_COMPLEX
    # 加载分类器，该类中封装的目标检测机制是晃动窗口机制+级联分类器的方式
    face_detector = cv2.CascadeClassifier(
        r'C:\Users\llh\Anaconda3\envs\py36\Lib\site-packages\cv2\data' +
        '\haarcascade_frontalface_default.xml')
    print('输入想增加的人脸及信息')
    face_id = input('\n enter id:')
    face_name = input('\n enter name:')
    new_people = pd.DataFrame({'id': [face_id], 'name': [face_name]})
    people_list = people_list.append(new_people)
    print('\n正在收集人脸信息，请注视摄像头......')
    count = 0
    while True:
        # 从摄像头读取图片
        sucess, img = cap.read()
        # 转为灰度图片
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0), 2)
            cv2.putText(img, str(count + 1) + ' faces collected' + '', (x, y), font, 0.8, (139, 139, 0), 2)
            count += 1
            # 保存图像
            ok = cv2.imwrite(
                r"C:/Users/llh/PycharmProjects/example_in_book/Face_detection/Facedate/Face." + str(
                    face_id) + '.' + str(
                    count) + '.jpg', gray[y: y + h, x: x + w])
            cv2.imshow('image', img)
        # 保持画面的持续。
        k = cv2.waitKey(1)
        if k == 27:  # 通过esc键退出摄像
            print('正在退出......')
            break
        elif count >= 500:  # 得到1000个样本后退出摄像
            print('收集完毕，正在退出......')
            break
    # 保存修改或新增的名单
    people_list.to_pickle(r'people_list.pkl')
    # 关闭摄像头
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    collect_face_data()
